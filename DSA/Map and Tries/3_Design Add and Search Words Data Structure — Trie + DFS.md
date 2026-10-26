# Design Add and Search Words Data Structure — Trie + DFS

## 1. Problem Statement

Design a data structure called `WordDictionary` that supports two operations:

1. `addWord(word)` — Add a word to the data structure.
2. `search(word)` — Search for a word, where `.` can represent **any single character**.

This problem is commonly known as **Design Add and Search Words Data Structure (LeetCode 211)**.

### Example

```python
wordDictionary = WordDictionary()

wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")

print(wordDictionary.search("pad"))  # False
print(wordDictionary.search("bad"))  # True
print(wordDictionary.search(".ad"))  # True
print(wordDictionary.search("b.."))  # True
```

### Understanding the Wildcard `.`

| Search | Result | Explanation |
|---|---|---|
| `"bad"` | `True` | Exact word exists |
| `"pad"` | `False` | No matching word |
| `".ad"` | `True` | `.` matches `b`, `d`, or `m` |
| `"b.."` | `True` | `.` matches any character at each position |
| `"..."` | `True` | Any stored word of length 3 matches |
| `".."` | `False` | No stored word has length 2 |

**Important:** The dot represents exactly one character, not zero or more characters.

---

## 2. Approach: Trie + DFS (Depth-First Search)

A normal Trie supports character-by-character searching. However, this problem introduces a wildcard character `.`.

When we encounter a normal character, we follow its corresponding child.

When we encounter `.`, we must explore **every available child** because any character can match.

We use DFS to explore these possible paths.

### Main Idea

1. Store every word in a Trie.
2. Search the word character by character.
3. If the current character is a normal character, follow that child.
4. If the current character is `.`, recursively explore every child.
5. When all search characters have been processed, return `True` only if the current node marks the end of a complete word.

---

## 3. Complete Python Code

```python
class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()

            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.is_end

            char = word[i]

            if char == '.':
                for ch in node.children.values():
                    if dfs(ch, i + 1):
                        return True

                return False

            if char not in node.children:
                return False

            return dfs(node.children[char], i + 1)

        return dfs(self, 0)
```

---

## 4. Understanding the Trie Structure

In this implementation, every `WordDictionary` object represents a Trie node.

```python
def __init__(self):
    self.children = {}
    self.is_end = False
```

### `children`

Stores the child nodes using a dictionary.

For example:

```python
{
    "b": WordDictionary(),
    "d": WordDictionary(),
    "m": WordDictionary()
}
```

This means the current node has three possible next characters.

### `is_end`

Indicates whether a complete word ends at the current node.

For example, if `"bad"` is inserted, the final `"d"` node has:

```python
is_end = True
```

This prevents a prefix such as `"ba"` from being incorrectly treated as a complete word.

---

## 5. Understanding `addWord(word)`

### Code

```python
def addWord(self, word: str) -> None:
    node = self

    for char in word:
        if char not in node.children:
            node.children[char] = WordDictionary()

        node = node.children[char]

    node.is_end = True
```

### Step-by-Step Explanation

**Step 1: Start at the root**

```python
node = self
```

**Step 2: Process each character**

```python
for char in word:
```

For `"bad"`, the characters are processed in this order:

```text
b → a → d
```

**Step 3: Create a node if the character does not exist**

```python
if char not in node.children:
    node.children[char] = WordDictionary()
```

If the child already exists, reuse it. This allows multiple words to share common prefixes.

**Step 4: Move to the child**

```python
node = node.children[char]
```

**Step 5: Mark the end of the word**

```python
node.is_end = True
```

This tells the Trie that a complete word ends at this node.

### Dry Run

Insert:

```python
addWord("bad")
addWord("bag")
```

The Trie shares the prefix `"ba"`.

```text
root
  |
  b
  |
  a
 / \
d   g
```

Both `"d"` and `"g"` are marked as word endings.

### Complexity

Let `L` be the length of the inserted word.

- Time: `O(L)` average.
- Additional space: `O(L)` in the worst case if every character requires a new node.

---

## 6. Understanding `search(word)`

The search operation is the most important part of this problem.

```python
def search(self, word: str) -> bool:

    def dfs(node, i):
        if i == len(word):
            return node.is_end

        char = word[i]

        if char == '.':
            for ch in node.children.values():
                if dfs(ch, i + 1):
                    return True

            return False

        if char not in node.children:
            return False

        return dfs(node.children[char], i + 1)

    return dfs(self, 0)
```

The nested `dfs()` function receives:

- `node`: The current Trie node.
- `i`: The index of the character currently being searched.

Instead of moving through only one path, DFS can explore multiple paths when it encounters `.`.

### Case 1: Base Case

```python
if i == len(word):
    return node.is_end
```

This condition checks whether every character in the search pattern has been processed.

If `i` reaches the length of `word`, there are no more characters to match.

However, we must still check:

```python
return node.is_end
```

Why?

Because the path might exist without representing a complete word.

For example, if `"bad"` is stored:

```python
search("ba")  # False
```

The path `"ba"` exists, but `"ba"` was not inserted as a complete word.

### Case 2: Get the Current Character

```python
char = word[i]
```

This retrieves the character at the current index.

For example, when searching `"b.d"`:

```text
i = 0 → b
i = 1 → .
i = 2 → d
```

### Case 3: Handle the Wildcard `.`

```python
if char == '.':
    for ch in node.children.values():
        if dfs(ch, i + 1):
            return True

    return False
```

This is the key logic.

The dot can match any single character, so we cannot choose just one child.

Instead, we explore all available child nodes.

**Step 1: Explore each child**

```python
for ch in node.children.values():
```

Each `ch` is a child Trie node, not the character itself.

**Step 2: Move to the next pattern character**

```python
dfs(ch, i + 1)
```

Because the dot matches one character, we advance the search index by one.

**Step 3: Stop if any path succeeds**

```python
if dfs(ch, i + 1):
    return True
```

If any child leads to a complete matching word, the search succeeds.

**Step 4: Return `False` if all paths fail**

```python
return False
```

If no child leads to a match, the wildcard cannot be satisfied at this position.

### Case 4: Handle a Normal Character

```python
if char not in node.children:
    return False
```

If the required character does not exist, there is no possible match along this path.

Otherwise, continue through the matching child:

```python
return dfs(node.children[char], i + 1)
```

We follow only one child because a normal character specifies exactly which character must match.

---

## 7. Dry Run 1: Exact Word Search

Suppose we insert:

```python
addWord("bad")
addWord("dad")
addWord("mad")
```

Now search:

```python
search("bad")
```

### Execution

```text
dfs(root, 0)
```

Current character is `"b"`.

- `"b"` exists in `root.children`.
- Follow the `"b"` child.

```text
dfs(b_node, 1)
```

Current character is `"a"`.

- `"a"` exists.
- Follow the `"a"` child.

```text
dfs(a_node, 2)
```

Current character is `"d"`.

- `"d"` exists.
- Follow the `"d"` child.

```text
dfs(d_node, 3)
```

Now:

```python
i == len("bad")
```

The base case returns:

```python
node.is_end  # True
```

**Final result: `True`**

---

## 8. Dry Run 2: Search With a Wildcard

Search:

```python
search(".ad")
```

Stored words:

```python
["bad", "dad", "mad"]
```

### Step 1: Process `.`

```python
char = word[0]  # "."
```

Since the current character is `.`, DFS explores every child of the root.

```text
             root
           /  |  \
          b   d   m
```

The search now explores three possible paths:

```text
b → a → d
d → a → d
m → a → d
```

### Step 2: Match the Remaining Characters

For each child, the next required character is `"a"`.

Each path is explored recursively.

Then the next required character is `"d"`.

All three words are complete matches.

As soon as the first successful path is found, the search returns `True`.

**Final result: `True`**

The important point is that the dot causes branching, while normal characters follow a specific path.

---

## 9. Dry Run 3: Search With Multiple Wildcards

Search:

```python
search("b..")
```

Suppose these words are stored:

```python
["bad", "bag", "bat", "dad"]
```

### Step 1: Match `"b"`

The first character is normal, so follow only the `"b"` child.

### Step 2: Match the First `.`

Explore every child below `"b"`.

For example:

```text
b
|
a
/|\
d g t
```

Each child can match the second pattern character.

### Step 3: Match the Second `.`

The search advances one character for each recursive call.

When it reaches the end of the pattern, it checks `node.is_end`.

Because `"bad"`, `"bag"`, and `"bat"` are stored complete words, the search returns `True`.

```python
search("b..")  # True
```

---

## 10. Why Do We Use DFS?

Without wildcards, searching a Trie is straightforward: each character selects one child.

With a wildcard, several children might match the current position.

Consider:

```python
search(".ad")
```

The first character could be `"b"`, `"d"`, `"m"`, or any other child available at the root.

DFS explores one possibility at a time.

```text
               root
             /  |  \
            b   d   m
            |   |   |
            a   a   a
            |   |   |
            d   d   d
```

DFS is appropriate because:

1. Each wildcard can create multiple possible paths.
2. Each path must be checked recursively.
3. A successful path allows the algorithm to return immediately.
4. If every path fails, the search returns `False`.

**Key idea:** Normal characters follow one path; wildcards explore multiple paths.

---

## 11. Time and Space Complexity

Let:

- `L` = length of the inserted word.
- `M` = length of the search pattern.
- `N` = number of words stored in the Trie.
- `B` = branching factor, or the number of possible child characters at a node.

### `addWord(word)`

Every character is processed once.

- Time: `O(L)` average.
- Additional space: `O(L)` in the worst case.

### `search(word)`

**Without wildcards:**

Each character follows one path.

- Time: `O(M)` average.
- Recursive stack space: `O(M)`.

**With wildcards:**

A wildcard can explore multiple child nodes.

If the Trie branches significantly at wildcard positions, many paths may be explored.

A general upper bound for a Trie with branching factor `B` is:

\[
O(B^M)
\]

This is a loose worst-case upper bound on the number of explored paths. The actual work is limited by the nodes and paths present in the Trie.

- Recursive stack space: `O(M)`, since each recursive call advances the pattern index.
- Additional search space excludes the already stored Trie.

---

## 12. Common Mistakes

### Mistake 1: Treating `.` as a Normal Character

Incorrect:

```python
if char not in node.children:
    return False
```

If applied to `.`, this would search for a literal dot rather than a wildcard.

Correct:

```python
if char == '.':
    for ch in node.children.values():
        if dfs(ch, i + 1):
            return True

    return False
```

### Mistake 2: Advancing the Index Incorrectly

Correct:

```python
dfs(ch, i + 1)
```

The wildcard represents exactly one character, so the pattern index must advance by one.

### Mistake 3: Returning `True` at the Base Case

Incorrect:

```python
if i == len(word):
    return True
```

This could incorrectly accept a prefix that is not a complete word.

Correct:

```python
if i == len(word):
    return node.is_end
```

### Mistake 4: Returning `False` After Only One Wildcard Branch Fails

Incorrect logic would stop after checking the first child and finding no match.

Instead, try every child and return `False` only after all possible branches fail.

### Mistake 5: Confusing Child Nodes With Characters

```python
for ch in node.children.values():
```

Here, `ch` represents a child node.

By contrast:

```python
for char in node.children:
```

iterates over the dictionary's character keys.

Both are valid, but the distinction is important.

---

## 13. Quick Revision Cheat Sheet

| Concept | Remember |
|---|---|
| Trie | Stores words character by character |
| `children` | Dictionary of child nodes |
| `is_end` | Marks a complete word |
| `addWord()` | Insert characters and mark the final node |
| Normal character | Follow the matching child |
| Wildcard `.` | Explore every child using DFS |
| Base case | Return `node.is_end` |
| Early success | Return `True` as soon as any branch succeeds |
| All branches fail | Return `False` |
| Exact search | `O(M)` average |
| Wildcard search | May explore many paths; exponential upper bound in pattern length |

## One-Line Pattern

**Trie + DFS wildcard pattern:** Follow the matching child for normal characters; when encountering `.`, recursively explore every child and succeed if any path ends at a complete word.