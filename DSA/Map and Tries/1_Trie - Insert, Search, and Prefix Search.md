# Trie - Insert, Search, and Prefix Search

## 1. Problem Statement

Implement a **Trie (Prefix Tree)** that supports three operations:

1. `insert(word)` — Insert a word into the Trie.
2. `search(word)` — Check whether a complete word exists in the Trie.
3. `startsWith(prefix)` — Check whether any word starts with the given prefix.

### Example

```python
trie = Trie()

trie.insert("apple")

print(trie.search("apple"))    # True
print(trie.search("app"))      # False
print(trie.startsWith("app"))  # True

trie.insert("app")

print(trie.search("app"))      # True
```

**Important distinction:**
- `search("app")` returns `False` if `"app"` is only a prefix of another word and has not been inserted as a complete word.
- `startsWith("app")` returns `True` if the prefix exists in the Trie, even if it is not a complete word.

---

## 2. What Is a Trie?

A **Trie**, also called a **Prefix Tree**, is a tree-like data structure used to store strings character by character.

For example, if we insert `"cat"`, `"car"`, and `"care"`, the Trie shares the common prefix `"ca"`.

```text
          root
           |
           c
           |
           a
          / \
         t   r
        (end) |
              e
             (end)
```

The diagram is simplified. The actual Trie also stores information indicating which nodes mark the end of a complete word.

### Why Use a Trie?

- Efficient prefix searching.
- Avoids storing repeated prefixes separately.
- Useful for autocomplete and dictionary problems.
- Can search words by traversing their characters.

---

## 3. Understanding the TrieNode Structure

In this implementation, every `Trie` object represents a node.

```python
class Trie:

    def __init__(self):
        self.children = {}
        self.is_end = False
```

### `children`

```python
self.children = {}
```

A dictionary that stores the child nodes of the current node.

- Key: a character.
- Value: the Trie node corresponding to that character.

For example:

```python
{
    "a": Trie(),
    "b": Trie()
}
```

This means the current node has two children: `"a"` and `"b"`.

### `is_end`

```python
self.is_end = False
```

Indicates whether the current node represents the end of a complete word.

Consider inserting `"apple"`:

```text
root → a → p → p → l → e
                              |
                         is_end = True
```

The final `"e"` node has `is_end = True`.

If `"app"` has not been inserted separately, the second `"p"` node has `is_end = False`.

**Key idea:** A character path can exist without representing a complete word.

---

## 4. Complete Code

```python
class Trie:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = Trie()

            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True
```

---

## 5. Understanding `insert(word)`

### Code

```python
def insert(self, word: str) -> None:
    node = self

    for char in word:
        if char not in node.children:
            node.children[char] = Trie()

        node = node.children[char]

    node.is_end = True
```

### Step-by-step explanation

**Step 1: Start from the root**

```python
node = self
```

`self` represents the root Trie node when the operation is called on the main Trie object.

We use `node` to traverse the Trie without losing the root reference.

**Step 2: Traverse each character**

```python
for char in word:
```

If the word is `"cat"`, the loop processes:

```text
c → a → t
```

**Step 3: Create a node if it does not exist**

```python
if char not in node.children:
    node.children[char] = Trie()
```

If the current character is missing, create a new Trie node for it.

If it already exists, reuse that node. This is how common prefixes are shared.

**Step 4: Move to the child node**

```python
node = node.children[char]
```

Move the pointer to the node representing the current character.

**Step 5: Mark the end of the word**

```python
node.is_end = True
```

After processing all characters, mark the last node as the end of a complete word.

### Dry Run: Insert `"cat"`

Initially:

```text
root
```

Process `"c"`:

```text
root
  |
  c
```

Process `"a"`:

```text
root
  |
  c
  |
  a
```

Process `"t"` and mark its node as the end:

```text
root
  |
  c
  |
  a
  |
  t  ← is_end = True
```

The word `"cat"` is now stored.

---

## 6. Understanding `search(word)`

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

### Step-by-step explanation

**Step 1:** Start from the root.

```python
node = self
```

**Step 2:** Traverse each character.

```python
for char in word:
```

**Step 3:** If any character is missing, the word does not exist.

```python
if char not in node.children:
    return False
```

**Step 4:** Move to the next node.

```python
node = node.children[char]
```

**Step 5:** After traversing every character, check whether the last node marks the end of a word.

```python
return node.is_end
```

This final line is the most important part of `search()`.

### Dry Run

Suppose `"apple"` has been inserted.

**Case 1: `search("apple")`**

Every character exists, and the final `"e"` node has `is_end = True`.

Result:

```python
True
```

**Case 2: `search("app")`**

Every character exists, but the final `"p"` node has `is_end = False` if `"app"` was never inserted.

Result:

```python
False
```

**Case 3: `search("bat")`**

The first character `"b"` does not exist in the root's children.

Result:

```python
False
```

### Why Return `node.is_end` Instead of `True`?

Because finding the character path does not necessarily mean the complete word was inserted.

```python
return node.is_end
```

checks both the existence of the path and the existence of the complete word.

---

## 7. Understanding `startsWith(prefix)`

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

### Step-by-step explanation

The logic is similar to `search()`, but there is one important difference.

- `search()` checks whether the final node represents a complete word.
- `startsWith()` only checks whether the entire prefix path exists.

Notice the final line:

```python
return True
```

We do not check `node.is_end`.

### Dry Run

Suppose `"apple"` has been inserted.

Call:

```python
trie.startsWith("app")
```

Traversal:

```text
root → a → p → p
```

All characters exist, so the method returns:

```python
True
```

Even if `"app"` was never inserted as a complete word, it is still a valid prefix of `"apple"`.

Now call:

```python
trie.startsWith("bat")
```

If `"b"` is missing, the method returns:

```python
False
```

---

## 8. Understanding the Difference Between `search()` and `startsWith()`

Assume only `"apple"` has been inserted.

| Operation | Result | Reason |
|---|---|---|
| `search("apple")` | `True` | Complete word exists |
| `search("app")` | `False` | Prefix exists, but not a complete word |
| `startsWith("app")` | `True` | Prefix path exists |
| `startsWith("apple")` | `True` | Entire path exists |
| `search("bat")` | `False` | Character path is missing |
| `startsWith("bat")` | `False` | Prefix path is missing |

**Interview takeaway:** Both methods traverse the Trie. The difference is what they check after traversal.

---

## 9. Time and Space Complexity

Let `L` be the length of the word or prefix being processed.

| Operation | Time Complexity | Explanation |
|---|---|---|
| `insert(word)` | `O(L)` average | Processes each character once |
| `search(word)` | `O(L)` average | Traverses each character once |
| `startsWith(prefix)` | `O(L)` average | Traverses each prefix character once |

These bounds assume average-case dictionary operations take `O(1)` time.

### Space Complexity

Each newly created character node requires additional space.

- Inserting one word of length `L` can create at most `L` new nodes.
- Across all inserted words, total Trie storage is proportional to the number of distinct prefixes, bounded by the total number of characters inserted.

For `N` inserted words with total length `S`, the worst-case space complexity is:

\[
O(S)
\]

---

## 10. Common Mistakes

### Mistake 1: Forgetting `is_end = True`

Incorrect:

```python
node = node.children[char]
```

If you never mark the final node, `search()` will return `False` for inserted words.

Correct:

```python
node.is_end = True
```

### Mistake 2: Returning `True` From `search()` Without Checking `is_end`

Incorrect:

```python
return True
```

This incorrectly treats every valid prefix as a complete word.

Correct:

```python
return node.is_end
```

### Mistake 3: Checking `is_end` in `startsWith()`

Incorrect:

```python
return node.is_end
```

This rejects valid prefixes that are not complete words.

Correct:

```python
return True
```

Once all prefix characters have been found, the prefix exists.

### Mistake 4: Forgetting to Move to the Child

Incorrect:

```python
if char not in node.children:
    return False
```

If you never update `node`, the traversal cannot progress.

Correct:

```python
node = node.children[char]
```

### Mistake 5: Creating a New Node Even When the Character Exists

Always reusing existing child nodes allows words with common prefixes to share the same path.

---

## 11. Important Interview Questions

Practice these Trie problems:

1. Implement Trie (Prefix Tree).
2. Design Add and Search Words Data Structure.
3. Replace Words.
4. Search Suggestions System.
5. Longest Word in Dictionary.
6. Word Search II.
7. Maximum XOR of Two Numbers in an Array.

---

## 12. Quick Revision Cheat Sheet

| Concept | Remember |
|---|---|
| `children` | Dictionary of child nodes |
| `is_end` | Marks the end of a complete word |
| `insert()` | Create missing nodes and mark the final node |
| `search()` | Traverse and return `node.is_end` |
| `startsWith()` | Traverse and return `True` if the path exists |
| Shared prefix | Existing nodes are reused |
| Time complexity | `O(L)` per operation, on average |
| Total space | `O(S)` for `S` total inserted characters, as an upper bound |

## One-Line Pattern

**Trie pattern:** Traverse character by character using a dictionary of child nodes; use `is_end` to distinguish a complete word from a prefix.