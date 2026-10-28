# Replace Words — Trie + Prefix Search

## 1. Problem Statement

Given a `dictionary` containing root words and a `sentence`, replace every word in the sentence with the **shortest root that is a prefix of that word**.

If no root matches a word, keep the original word unchanged.

This problem is commonly known as **Replace Words (LeetCode 648)**.

### Example

**Input:**

```python
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
```

**Output:**

```text
the cat was rat by the bat
```

### Explanation

- `"cattle"` starts with `"cat"` → replace with `"cat"`.
- `"rattled"` starts with `"rat"` → replace with `"rat"`.
- `"battery"` starts with `"bat"` → replace with `"bat"`.
- Words without a matching root remain unchanged.

**Important:** Always choose the shortest matching root.

---

## 2. Approach: Trie

A Trie stores dictionary roots character by character.

For each word in the sentence:

1. Start from the Trie root.
2. Traverse the word character by character.
3. Build the prefix as we traverse.
4. If a node has `is_end = True`, we have found a complete dictionary root.
5. Replace the word immediately with that prefix.
6. If no root is found, keep the original word.

### Why Does This Work?

The Trie lets us identify the shortest matching root because we stop as soon as we reach a node marked as the end of a dictionary word.

For example, if the dictionary contains:

```python
["cat", "cattle"]
```

For the word `"cattle"`, we stop at `"cat"` because it is already a complete root.

We do not continue searching for `"cattle"`.

---

## 3. Complete Python Code

```python
class Solution:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, dictionary):
        for words in dictionary:
            node = self

            for char in words:
                if char not in node.children:
                    node.children[char] = Solution()

                node = node.children[char]

            node.is_end = True

    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        self.insert(dictionary)

        ans = []

        word = sentence.split()

        for char in word:
            node = self
            prefix = ""
            found = False

            for ch in char:
                if ch not in node.children:
                    break

                prefix += ch
                node = node.children[ch]

                if node.is_end:
                    ans.append(prefix)
                    found = True
                    break

            if not found:
                ans.append(char)

        return " ".join(ans)
```

---

## 4. Understanding the Trie Structure

### Node Initialization

```python
def __init__(self):
    self.children = {}
    self.is_end = False
```

Each node contains:

- `children`: A dictionary containing child nodes.
- `is_end`: Indicates whether a complete dictionary root ends at this node.

For example, inserting `"cat"` creates the path:

```text
root
 |
 c
 |
 a
 |
 t  ← is_end = True
```

The `is_end` flag tells us that `"cat"` is a complete root.

---

## 5. Understanding `insert(dictionary)`

### Code

```python
def insert(self, dictionary):
    for words in dictionary:
        node = self

        for char in words:
            if char not in node.children:
                node.children[char] = Solution()

            node = node.children[char]

        node.is_end = True
```

### Step-by-Step Explanation

**Step 1: Iterate over every root**

```python
for words in dictionary:
```

For example:

```python
dictionary = ["cat", "bat", "rat"]
```

Each root is inserted into the Trie.

**Step 2: Start from the root**

```python
node = self
```

**Step 3: Process each character**

```python
for char in words:
```

For `"cat"`:

```text
c → a → t
```

**Step 4: Create a node if necessary**

```python
if char not in node.children:
    node.children[char] = Solution()
```

If the character already exists, reuse the existing node.

**Step 5: Move to the child node**

```python
node = node.children[char]
```

**Step 6: Mark the end of the root**

```python
node.is_end = True
```

This allows the search to identify a complete dictionary root.

### Complexity

Let `D` be the total number of characters across all dictionary roots.

- Time: `O(D)` average.
- Space: `O(D)` in the worst case.

---

## 6. Understanding `replaceWords()`

### Step 1: Build the Trie

```python
self.insert(dictionary)
```

Insert all dictionary roots before processing the sentence.

### Step 2: Initialize the Result List

```python
ans = []
```

This list stores the final words after replacement.

### Step 3: Split the Sentence

```python
word = sentence.split()
```

For:

```python
sentence = "the cattle was rattled"
```

The result is:

```python
["the", "cattle", "was", "rattled"]
```

### Step 4: Process Every Word

```python
for char in word:
```

Here, `char` represents an entire word, not a single character.

For example:

```python
char = "cattle"
```

For readability, you could rename this variable to `current_word`.

### Step 5: Initialize the Search

```python
node = self
prefix = ""
found = False
```

- `node`: Tracks the current position in the Trie.
- `prefix`: Stores the characters traversed so far.
- `found`: Indicates whether a matching root has been found.

These variables are reset for every word.

### Step 6: Traverse the Word

```python
for ch in char:
    if ch not in node.children:
        break

    prefix += ch
    node = node.children[ch]
```

For `"cattle"`, the prefix grows as follows:

```text
c → ca → cat → catt → ...
```

If a character is missing from the Trie, the search stops because no dictionary root can match the word beyond that point.

### Step 7: Stop at the First Complete Root

```python
if node.is_end:
    ans.append(prefix)
    found = True
    break
```

This is the most important part of the solution.

As soon as `node.is_end` becomes `True`, we have found a dictionary root.

We append that prefix to the result and stop searching the current word.

**Why break immediately?**

Because the first complete root encountered is the shortest matching root.

### Step 8: Keep the Original Word if No Root Matches

```python
if not found:
    ans.append(char)
```

If the Trie traversal fails or finishes without finding a complete root, append the original word.

### Step 9: Join the Words

```python
return " ".join(ans)
```

Join all resulting words with spaces to produce the final sentence.

---

## 7. Dry Run

Consider:

```python
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
```

### Step 1: Insert the Roots

The Trie stores:

```text
root
├── c → a → t*
├── b → a → t*
└── r → a → t*
```

`*` indicates `is_end = True`.

### Step 2: Process Each Word

**Word 1: `"the"`**

- The first character `"t"` does not exist at the root.
- No root matches.

Result:

```python
"the"
```

**Word 2: `"cattle"`**

Traversal:

```text
c → a → t
```

At `"cat"`:

```python
node.is_end = True
```

Append `"cat"` and stop.

Result:

```python
"cat"
```

**Word 3: `"was"`**

- The first character `"w"` is missing.
- Keep the original word.

Result:

```python
"was"
```

**Word 4: `"rattled"`**

Traversal:

```text
r → a → t
```

At `"rat"`, `is_end = True`.

Result:

```python
"rat"
```

**Word 5: `"by"`**

- No matching root.
- Keep `"by"`.

**Word 6: `"the"`**

- No matching root.
- Keep `"the"`.

**Word 7: `"battery"`**

Traversal:

```text
b → a → t
```

At `"bat"`, `is_end = True`.

Result:

```python
"bat"
```

### Final Output

```text
the cat was rat by the bat
```

---

## 8. Why Does This Find the Shortest Root?

Suppose the dictionary contains:

```python
dictionary = ["a", "ap", "app", "apple"]
sentence = "apple"
```

The Trie contains all four roots.

While searching `"apple"`:

1. Reach `"a"` — `is_end = True`.
2. Append `"a"` to the answer.
3. Stop searching this word.

The output is:

```text
a
```

Even though `"ap"`, `"app"`, and `"apple"` are also roots, `"a"` is the shortest matching root.

**Key idea:** Traverse from left to right and stop at the first node marked as the end of a dictionary root.

---

## 9. Time and Space Complexity

Let:

- `D` = total number of characters across all dictionary roots.
- `T` = total number of characters across all words in the sentence.
- `W` = number of words in the sentence.

### Building the Trie

Every dictionary character is processed once.

\[
O(D)
\]

### Processing the Sentence

Every word is traversed until a root is found or a character is missing.

Across all words, at most the total number of sentence characters is traversed.

\[
O(T)
\]

The `prefix += ch` operation can copy strings in Python. A strict character-copying analysis may add overhead, but the overall algorithm remains linear in the input size for typical bounded-length words.

### Total Time Complexity

\[
O(D + T)
\]

### Space Complexity

- Trie storage: `O(D)`.
- Result list and split words: `O(T)`.

Overall auxiliary space:

\[
O(D + T)
\]

---

## 10. Common Mistakes

### Mistake 1: Forgetting to Mark the Root's End

Incorrect:

```python
node = node.children[char]
```

Without marking the final node, the algorithm cannot recognize a complete root.

Correct:

```python
node.is_end = True
```

### Mistake 2: Continuing After Finding a Root

Incorrect logic continues traversing after finding `"cat"` in `"cattle"`.

Correct:

```python
if node.is_end:
    ans.append(prefix)
    found = True
    break
```

The first complete root is the shortest matching root.

### Mistake 3: Forgetting to Reset the Prefix

```python
prefix = ""
```

This must be initialized for every word. Otherwise, characters from previous words could affect the current result.

### Mistake 4: Forgetting the `found` Flag

If no root matches, the original word must be appended.

```python
if not found:
    ans.append(char)
```

### Mistake 5: Confusing a Prefix With a Complete Root

A word may follow a valid Trie path without reaching a node where `is_end = True`.

Only a complete dictionary root can replace the original word.

---

## 11. Quick Revision Cheat Sheet

| Concept | Remember |
|---|---|
| Trie | Stores dictionary roots character by character |
| `insert()` | Creates nodes and marks the end of every root |
| Prefix traversal | Search the sentence word character by character |
| `is_end` | Indicates a complete root |
| Shortest root | Stop at the first `is_end = True` node |
| `found` | Tracks whether a root was discovered |
| No matching root | Keep the original word |
| Time complexity | `O(D + T)` |
| Space complexity | `O(D + T)` including the result and split words |

## One-Line Pattern

**Replace Words pattern:** Insert dictionary roots into a Trie, traverse each sentence word, and replace it with the first complete root encountered.