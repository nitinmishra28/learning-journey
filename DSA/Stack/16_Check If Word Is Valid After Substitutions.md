# 1003. Check If Word Is Valid After Substitutions

## Problem

Given a string `s`, repeatedly remove the substring `"abc"` whenever it appears.

Return `True` if the string becomes empty; otherwise, return `False`.

---

# Brute Force

## Idea

* Scan the string and find `"abc"`.
* Remove every occurrence.
* Repeat until no `"abc"` exists.
* If the final string is empty, return `True`; otherwise, return `False`.

## Code

```python
class Solution:
    def isValid(self, s: str) -> bool:

        while True:
            found = False
            new_s = ""
            i = 0

            while i < len(s):
                if i + 2 < len(s) and s[i:i+3] == "abc":
                    found = True
                    i += 3
                else:
                    new_s += s[i]
                    i += 1

            if not found:
                break

            s = new_s

        return s == ""
```

### Complexity

* **Time:** `O(n²)`
* **Space:** `O(n)`

### Why is it slow?

The string is scanned multiple times, and a new string is created after every pass.

---

# Pattern

```text
Stack + Pattern Elimination (Continuous Pattern Reduction)
```

---

# Main Idea

* Traverse the string once.
* Push every character into a stack.
* Whenever the last **3** characters become `"abc"`, remove them immediately.
* If the stack is empty after processing all characters, the string is valid.

---

# Optimal Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            stack.append(ch)

            if (
                len(stack) >= 3
                and stack[-3] == 'a'
                and stack[-2] == 'b'
                and stack[-1] == 'c'
            ):
                stack.pop()
                stack.pop()
                stack.pop()

        return len(stack) == 0
```

---

# Why This Works

* Every new `"abc"` must include the **latest inserted character**.
* Therefore, checking only the **top 3** stack elements is sufficient.
* Removing one `"abc"` may create another `"abc"` automatically (chain reaction), which the stack naturally handles.
* Each character is pushed once and popped at most once.

---

# Dry Run

Input

```text
aabcbc
```

| Character | Stack | Action               |
| --------- | ----- | -------------------- |
| a         | a     | Push                 |
| a         | aa    | Push                 |
| b         | aab   | Push                 |
| c         | aabc  | Remove `abc` → `a`   |
| b         | ab    | Push                 |
| c         | abc   | Remove `abc` → Empty |

Final Stack

```text
Empty
```

Answer

```text
True
```

---

# Common Mistakes

### 1. Checking before pushing

❌ Wrong

```python
check()
stack.append(ch)
```

✅ Correct

```python
stack.append(ch)
check()
```

---

### 2. Forgetting `len(stack) >= 3`

Always check the size before accessing

```python
stack[-3]
```

---

### 3. Scanning the whole stack

Only the **last 3 characters** can form a new `"abc"`.

---

### 4. Removing only one character

Remove **all three** characters together.

---

# Complexity Comparison

| Approach                    | Time      | Space    |
| --------------------------- | --------- | -------- |
| Brute Force                 | **O(n²)** | **O(n)** |
| Stack + Pattern Elimination | **O(n)**  | **O(n)** |

---

# Pattern Recognition

Use this pattern when:

* A fixed substring is removed repeatedly.
* Removing one pattern may create another.
* Characters are processed sequentially.
* Only recently added characters affect future operations.

Similar Problems:

* Remove All Adjacent Duplicates
* Remove All Adjacent Duplicates II
* Valid Parentheses
* Basic Calculator

---

# Revision Cheat Sheet

```text
Pattern:
Stack + Pattern Elimination

Algorithm:
1. Push every character.
2. Check the top 3 characters.
3. If they form "abc", remove them.
4. Continue until the string ends.
5. Empty stack ⇒ Valid.

Brute Force:
Repeatedly remove "abc" until no removal is possible.

Time:
Brute Force → O(n²)
Optimal → O(n)

Space:
O(n)
```
