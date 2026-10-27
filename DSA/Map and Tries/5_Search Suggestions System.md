# Search Suggestions System — Trie + Sorting + DFS

## 1. Problem Statement

Given an array of product names `products` and a string `searchWord`, return a list of suggestions for every prefix of `searchWord`.

After each character of `searchWord` is typed:

1. Find products that start with the current prefix.
2. Return at most three matching products.
3. Return suggestions in **lexicographical (dictionary) order**.

This problem is commonly known as **Search Suggestions System (LeetCode 1268)**.

### Example

**Input:**

```python
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
```

**Output:**

```python
[
    ["mobile", "moneypot", "monitor"],
    ["mobile", "moneypot", "monitor"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"]
]
```

**Explanation:**

After typing each character:

| Typed prefix | Suggestions |
|---|---|
| `"m"` | `["mobile", "moneypot", "monitor"]` |
| `"mo"` | `["mobile", "moneypot", "monitor"]` |
| `"mou"` | `["mouse", "mousepad"]` |
| `"mous"` | `["mouse", "mousepad"]` |
| `"mouse"` | `["mouse", "mousepad"]` |

The results contain at most three matching products, sorted alphabetically.

---

## 2. Approach: Trie + Sorting + DFS

We use three important concepts:

1. **Sorting:** Sort products alphabetically before inserting them.
2. **Trie:** Store products character by character to efficiently locate a prefix.
3. **DFS:** Collect up to three products starting from the prefix node.

### Overall Strategy

1. Sort the products.
2. Insert every product into the Trie.
3. Process `searchWord` one character at a time.
4. Build the current prefix.
5. Find the Trie node corresponding to that prefix.
6. Use DFS to collect the first three matching products in lexicographical order.
7. Append the suggestions to the result.

---

## 3. Complete Python Code

```python
class Solution:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, products):
        for product in products:
            node = self

            for char in product:
                if char not in node.children:
                    node.children[char] = Solution()

                node = node.children[char]

            node.is_end = True

    def autocomplete(self, prefix: str):
        node = self

        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        suggestions = []

        def collect(node, current_word):
            if node.is_end:
                suggestions.append(current_word)

            if len(suggestions) == 3:
                return

            for char in sorted(node.children):
                collect(node.children[char], current_word + char)

                if len(suggestions) == 3:
                    return

        collect(node, prefix)
        return suggestions

    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        products.sort()
        self.insert(products)

        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            result.append(self.autocomplete(prefix))

        return result
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

- `children`: A dictionary mapping characters to child nodes.
- `is_end`: Indicates whether a complete product ends at this node.

For example, inserting `"mobile"` creates the path:

```text
root → m → o → b → i → l → e
                              |
                         is_end = True
```

Products with common prefixes share nodes.

For example, `"mouse"` and `"mousepad"` share the path for `"mouse"`.

---

## 5. Understanding `insert(products)`

### Code

```python
def insert(self, products):
    for product in products:
        node = self

        for char in product:
            if char not in node.children:
                node.children[char] = Solution()

            node = node.children[char]

        node.is_end = True
```

### Step-by-Step Explanation

**Step 1: Process every product**

```python
for product in products:
```

Each product is inserted separately.

**Step 2: Start at the root**

```python
node = self
```

**Step 3: Process each character**

```python
for char in product:
```

For `"mouse"`, the characters are:

```text
m → o → u → s → e
```

**Step 4: Create a node if necessary**

```python
if char not in node.children:
    node.children[char] = Solution()
```

If the character already exists, reuse its node.

**Step 5: Move to the child**

```python
node = node.children[char]
```

**Step 6: Mark the product's end**

```python
node.is_end = True
```

This allows DFS to identify complete product names.

### Complexity

Let `S` be the total number of characters across all products.

- Time: `O(S)` average.
- Space: `O(S)` in the worst case.

---

## 6. Why Do We Sort the Products First?

In `suggestedProducts()`:

```python
products.sort()
self.insert(products)
```

Sorting ensures that products are inserted in alphabetical order.

For example:

```python
products = ["mousepad", "mobile", "monitor", "moneypot"]
products.sort()

print(products)
```

Output:

```python
["mobile", "moneypot", "monitor", "mousepad"]
```

However, sorting the products alone does not guarantee that the DFS will visit Trie children alphabetically.

That is why the autocomplete method also uses:

```python
for char in sorted(node.children):
```

This sorts the child characters at every node, ensuring that DFS explores branches in lexicographical order.

**Important:** Sorting both the products and child characters works correctly, but sorting the products is not strictly necessary for the DFS ordering in this implementation. The sorted child traversal determines the order of suggestions.

---

## 7. Understanding `autocomplete(prefix)`

### Code

```python
def autocomplete(self, prefix: str):
    node = self

    for char in prefix:
        if char not in node.children:
            return []

        node = node.children[char]

    suggestions = []

    def collect(node, current_word):
        if node.is_end:
            suggestions.append(current_word)

        if len(suggestions) == 3:
            return

        for char in sorted(node.children):
            collect(node.children[char], current_word + char)

            if len(suggestions) == 3:
                return

    collect(node, prefix)
    return suggestions
```

This method has two stages.

### Stage 1: Find the Prefix Node

```python
node = self

for char in prefix:
    if char not in node.children:
        return []

    node = node.children[char]
```

Suppose:

```python
prefix = "mou"
```

The traversal follows:

```text
root → m → o → u
```

If any character is missing, no product can match that prefix, so the method returns an empty list.

Otherwise, `node` points to the Trie node corresponding to `"mou"`.

### Stage 2: Collect Matching Products

```python
suggestions = []
```

This list stores the matching products.

The nested `collect()` function explores the subtree rooted at the prefix node.

#### Step 1: Add a Complete Product

```python
if node.is_end:
    suggestions.append(current_word)
```

If the current node marks the end of a product, add the complete product to the suggestions.

For example, if `"mouse"` has been inserted, the node corresponding to `"mouse"` has `is_end = True`.

#### Step 2: Stop After Three Suggestions

```python
if len(suggestions) == 3:
    return
```

The problem asks for at most three suggestions.

Once three products have been collected, further traversal is unnecessary.

#### Step 3: Explore Children Alphabetically

```python
for char in sorted(node.children):
```

The child characters are visited in sorted order.

For each child:

```python
collect(node.children[char], current_word + char)
```

The algorithm appends the character to the current word and recursively explores that subtree.

#### Step 4: Stop Traversal When Three Are Found

```python
if len(suggestions) == 3:
    return
```

This second check is important because the recursive call may have collected the third suggestion.

It allows the algorithm to stop exploring sibling branches immediately.

Finally:

```python
collect(node, prefix)
return suggestions
```

DFS begins at the prefix node, using the prefix itself as the starting word.

---

## 8. Understanding DFS With an Example

Suppose the Trie contains:

```python
products = [
    "mobile",
    "moneypot",
    "monitor",
    "mouse",
    "mousepad"
]
```

Call:

```python
autocomplete("mo")
```

The Trie traversal first reaches the node for `"mo"`.

The DFS explores child characters alphabetically.

```text
mo
├── b → mobile
├── n → moneypot
│       └── i → ...
└── u → mouse
```

The actual traversal follows the available characters in sorted order.

For prefix `"mo"`, the products are:

```python
["mobile", "moneypot", "monitor"]
```

Once three products are found, the traversal stops.

For prefix `"mou"`, the matching products are:

```python
["mouse", "mousepad"]
```

Only two products match, so both are returned.

---

## 9. Understanding `suggestedProducts()`

### Code

```python
def suggestedProducts(
    self, products: list[str], searchWord: str
) -> list[list[str]]:
    products.sort()
    self.insert(products)

    result = []
    prefix = ""

    for char in searchWord:
        prefix += char
        result.append(self.autocomplete(prefix))

    return result
```

This method coordinates the complete solution.

### Step 1: Sort the Products

```python
products.sort()
```

Sort the products alphabetically.

### Step 2: Build the Trie

```python
self.insert(products)
```

Insert every product into the Trie.

### Step 3: Initialize the Result

```python
result = []
prefix = ""
```

- `result` stores the suggestions for every prefix.
- `prefix` tracks the characters typed so far.

### Step 4: Process Every Character

```python
for char in searchWord:
    prefix += char
    result.append(self.autocomplete(prefix))
```

For:

```python
searchWord = "mouse"
```

The prefixes are generated as follows:

| Character typed | Current prefix |
|---|---|
| `m` | `"m"` |
| `o` | `"mo"` |
| `u` | `"mou"` |
| `s` | `"mous"` |
| `e` | `"mouse"` |

For each prefix, `autocomplete()` returns the matching products.

### Step 5: Return the Result

```python
return result
```

The output contains one list of suggestions for each character in `searchWord`.

---

## 10. Complete Dry Run

Consider:

```python
products = [
    "mobile",
    "mouse",
    "moneypot",
    "monitor",
    "mousepad"
]

searchWord = "mouse"
```

### Step 1: Sort Products

```python
[
    "mobile",
    "moneypot",
    "monitor",
    "mouse",
    "mousepad"
]
```

### Step 2: Build the Trie

Insert all five products.

Products with common prefixes share nodes, such as `"mouse"` and `"mousepad"`.

### Step 3: Process Each Prefix

**Prefix `"m"`**

Matching products:

```python
["mobile", "moneypot", "monitor", "mouse", "mousepad"]
```

Take the first three:

```python
["mobile", "moneypot", "monitor"]
```

**Prefix `"mo"`**

Matching products:

```python
["mobile", "moneypot", "monitor", "mouse", "mousepad"]
```

Take the first three:

```python
["mobile", "moneypot", "monitor"]
```

**Prefix `"mou"`**

Matching products:

```python
["mouse", "mousepad"]
```

Return both:

```python
["mouse", "mousepad"]
```

**Prefix `"mous"`**

```python
["mouse", "mousepad"]
```

**Prefix `"mouse"`**

```python
["mouse", "mousepad"]
```

### Final Output

```python
[
    ["mobile", "moneypot", "monitor"],
    ["mobile", "moneypot", "monitor"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"]
]
```

---

## 11. Why Do We Use a Trie Instead of Searching Every Product?

A simple solution could check every product against every prefix.

However, a Trie lets us navigate directly to the node corresponding to a prefix and explore only the matching subtree.

This is particularly useful when:
- The product list is large.
- Many search prefixes must be evaluated.
- Prefix-based searching is performed repeatedly.

The Trie avoids repeatedly scanning every product for every prefix, although building and traversing the Trie still requires time and memory.

---

## 12. Time and Space Complexity

Let:

- `N` = number of products.
- `S` = total number of characters across all products.
- `M` = length of `searchWord`.
- `P` = length of a particular prefix.
- `V` = number of Trie nodes visited during autocomplete collection.

### Sorting

```python
products.sort()
```

Sorting takes approximately:

\[
O(N \log N \cdot L)
\]

where `L` represents a characteristic product length; more precisely, string comparisons may examine multiple characters.

### Building the Trie

Every character is inserted once.

\[
O(S)
\]

### Finding a Prefix

The Trie traversal processes each character in the prefix.

\[
O(P)
\]

### Collecting Suggestions

DFS explores nodes under the prefix and stops after finding three products.

Its traversal work depends on the nodes visited before stopping. Since constructing `current_word + char` creates new strings, character-copying costs must also be considered.

A useful upper bound for one autocomplete call is `O(V × Lmax)`, where `Lmax` is the maximum product length.

### Overall

The main costs are:

- Sorting the products.
- Building the Trie.
- Finding each search prefix and collecting its suggestions.

A general bound is:

\[
O(N \log N \cdot L + S + M \cdot L_{\max})
\]

This is a conservative bound for the implementation, where `Lmax` is the maximum product length. The actual autocomplete work is often smaller because DFS stops after three suggestions.

### Space Complexity

The Trie stores at most `O(S)` character nodes in the worst case.

The output requires space for the returned suggestions.

- Trie: `O(S)`.
- Output: Depends on the number and lengths of returned suggestions.
- Recursive DFS stack: Up to the maximum product length.

---

## 13. Common Mistakes

### Mistake 1: Forgetting to Sort Child Characters

Incorrect:

```python
for char in node.children:
```

This does not explicitly guarantee lexicographical traversal.

Correct:

```python
for char in sorted(node.children):
```

### Mistake 2: Forgetting to Stop After Three Suggestions

Without the limit checks, DFS could collect every matching product.

Correct:

```python
if len(suggestions) == 3:
    return
```

### Mistake 3: Checking `is_end` After Traversing Children

The current product should be added when its node is visited, before exploring longer products.

Correct:

```python
if node.is_end:
    suggestions.append(current_word)
```

This ensures that a product such as `"mouse"` can be suggested before `"mousepad"`.

### Mistake 4: Returning Suggestions for the Entire Trie

Autocomplete must begin from the node corresponding to the requested prefix, not from the root.

### Mistake 5: Forgetting to Append Results for Every Prefix

Each character typed creates a new prefix and requires its own suggestion list.

```python
prefix += char
result.append(self.autocomplete(prefix))
```

---

## 14. Quick Revision Cheat Sheet

| Concept | Remember |
|---|---|
| Sorting | Helps establish alphabetical product order |
| Trie | Stores product names character by character |
| `insert()` | Creates missing nodes and marks complete products |
| `autocomplete()` | Finds the prefix node and collects matching products |
| DFS | Explores descendants to reconstruct complete product names |
| `sorted(node.children)` | Visits child characters alphabetically |
| `node.is_end` | Identifies a complete product |
| Suggestion limit | Stop after collecting three products |
| `suggestedProducts()` | Generates one result list per search prefix |
| Trie space | `O(S)` in the worst case |

## One-Line Pattern

**Search Suggestions pattern:** Build a Trie, process each search prefix, then use lexicographical DFS to collect at most three matching products.