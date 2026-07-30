# 394. Decode String

## Problem

Given an encoded string, decode it.

Encoding Rule:

```text
k[encoded_string]
```

means repeat `encoded_string` exactly `k` times.

Examples:

```text
Input:  "3[a]2[bc]"
Output: "aaabcbc"

Input:  "3[a2[c]]"
Output: "accaccacc"

Input:  "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

---

# Brute Force

## Idea

* Scan the string repeatedly.
* Find the innermost `k[...]`.
* Decode it.
* Replace it in the original string.
* Repeat until no brackets remain.

## Complexity

* **Time:** O(n²)
* **Space:** O(n)

## Why is it slow?

Each replacement creates a new string, and the entire string may be scanned multiple times.

---

# Pattern

```text
Stack + Nested String Simulation
```

---

# Main Idea

* Traverse the string character by character.
* Push everything into the stack.
* When `]` is found:

  * Extract the encoded string until `[`.
  * Remove `[`.
  * Extract the complete number before `[`.
  * Repeat the extracted string.
  * Push the decoded string back into the stack.
* At the end, join everything.

The stack automatically handles nested brackets because the **innermost expression is decoded first**.

---

# Optimal Solution

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:

            # Keep pushing until closing bracket
            if ch != ']':
                stack.append(ch)

            else:

                # Extract current string
                curr_str = ""
                while stack[-1] != '[':
                    curr_str = stack.pop() + curr_str

                # Remove '['
                stack.pop()

                # Extract complete number
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num

                # Repeat string
                curr_str = int(curr_num) * curr_str

                # Push decoded string
                stack.append(curr_str)

        return "".join(stack)
```

---

# Why This Works

* The first completed pattern is always the **innermost** one.
* A stack naturally processes nested structures in **Last-In First-Out (LIFO)** order.
* After decoding one block, it is pushed back and becomes part of the outer block.

Example

```text
3[a2[c]]

↓

2[c]

↓

cc

↓

3[acc]

↓

accaccacc
```

---

# Dry Run

Input

```text
3[a2[c]]
```

### Stack Progress

| Character | Stack       |
| --------- | ----------- |
| 3         | 3           |
| [         | 3 [         |
| a         | 3 [ a       |
| 2         | 3 [ a 2     |
| [         | 3 [ a 2 [   |
| c         | 3 [ a 2 [ c |
| ]         | 3 [ a cc    |
| ]         | accaccacc   |

Answer

```text
accaccacc
```

---

# Common Mistakes

### 1. Forgetting multi-digit numbers

❌ Wrong

```python
curr_num = stack.pop()
```

Fails for

```text
12[a]
```

Always extract **all consecutive digits**.

---

### 2. Building the string in reverse

❌ Wrong

```python
curr_str += stack.pop()
```

Characters come out in reverse order.

Correct

```python
curr_str = stack.pop() + curr_str
```

---

### 3. Forgetting to remove `'['`

Always pop `'['` after extracting the substring.

```python
stack.pop()
```

---

### 4. Not pushing the decoded string back

After decoding,

```text
abc

↓

abcabcabc
```

must be pushed back so that outer expressions can use it.

---

# Complexity Comparison

| Approach    | Time                           | Space |
| ----------- | ------------------------------ | ----- |
| Brute Force | O(n²)                          | O(n)  |
| Stack       | O(n) *(excluding output size)* | O(n)  |

> **Note:** If the decoded output itself has length **m**, the total runtime is better described as **O(n + m)** because constructing the final decoded string takes proportional time.

---

# Pattern Recognition

Use this pattern when:

* Nested brackets are present.
* Inner expressions must be processed before outer ones.
* Decoding or evaluating nested structures.
* Matching opening and closing symbols.

Similar Problems

* Valid Parentheses
* Basic Calculator
* Mini Parser
* Remove Invalid Parentheses
* Decode String

---

# Revision Cheat Sheet

```text
Pattern:
Stack + Nested String Simulation

Algorithm:
1. Push every character.
2. On ']':
   • Build string until '['
   • Remove '['
   • Build complete number
   • Repeat string
   • Push decoded string back
3. Join stack.

Important:
✔ Extract digits in reverse.
✔ Support multi-digit numbers.
✔ Decode inner block first.

Time:
O(n + output_length)

Space:
O(n)
```
