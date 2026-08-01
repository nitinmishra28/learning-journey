# 71. Simplify Path

## Problem

Given an **absolute Unix file path**, return its **canonical (simplified) path**.

Rules:

* `"."` → Current directory (ignore it).
* `".."` → Go back to the parent directory.
* Multiple `"/"` should be treated as a single `/`.
* The final path should:

  * Start with `/`
  * Not end with `/` (unless it is the root `/`)

### Examples

```text
Input : "/home/"
Output: "/home"
```

```text
Input : "/../"
Output: "/"
```

```text
Input : "/home//foo/"
Output: "/home/foo"
```

```text
Input : "/a/./b/../../c/"
Output: "/c"
```

---

# Brute Force

## Idea

* Split the path into directories.
* Store them in a list.
* Whenever `"."` or `".."` appears, repeatedly modify the list by deleting elements.
* Continue rebuilding the path until all operations are processed.

Since deleting elements from the middle of a list shifts remaining elements, this approach becomes inefficient.

---

## Brute Force Code

```python
class Solution:
    def simplifyPath(self, path: str) -> str:

        directories = path.split("/")
        result = []

        for directory in directories:

            if directory == "" or directory == ".":
                continue

            elif directory == "..":
                if result:
                    del result[-1]

            else:
                result.append(directory)

        return "/" + "/".join(result)
```

> **Note:** This solution works, but using `del` on a list behaves like stack operations here. Using an explicit stack (`append()` / `pop()`) is clearer and directly matches the problem pattern.

---

## Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

Although often called a brute-force approach, it is still linear because each directory is processed only once.

---

# Pattern

```text
Stack + Path Simulation
```

---

# Main Idea

Think of every directory as entering a folder.

* Normal directory → Go inside → Push into stack.
* `"."` → Stay in the same folder → Ignore.
* `".."` → Go back one folder → Pop from stack.
* Empty string (created by multiple `/`) → Ignore.

After processing all directories, join the stack to form the simplified path.

---

# Optimal Solution

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        directories = path.split("/")

        for directory in directories:

            # Ignore empty directory and "."
            if directory == "" or directory == ".":
                continue

            # Go to parent directory
            elif directory == "..":
                if stack:
                    stack.pop()

            # Valid directory
            else:
                stack.append(directory)

        return "/" + "/".join(stack)
```

---

# Why `split("/")`?

Example

```text
/home//foo/../user/
```

After splitting

```python
path.split("/")
```

we get

```python
["", "home", "", "foo", "..", "user", ""]
```

Notice:

* Leading `/` creates an empty string.
* Multiple `/` create empty strings.
* Trailing `/` also creates an empty string.

Therefore, we ignore

```python
""
```

during traversal.

---

# Why Ignore `"."`?

```text
/home/./user
```

`.` means

> Stay in the current directory.

So

```text
/home/./user
```

is exactly the same as

```text
/home/user
```

Hence we simply

```python
continue
```

---

# Why Pop for `".."`?

Suppose the path is

```text
/home/user/docs/..
```

Current stack

```text
home
user
docs
```

`".."`
means

> Go to the parent directory.

So we remove

```text
docs
```

using

```python
stack.pop()
```

Stack becomes

```text
home
user
```

Exactly the expected path.
