# 1472. Design Browser History

## Problem

Design a browser history system that supports the following operations:

* `visit(url)` → Visit a new webpage.
* `back(steps)` → Move back by at most `steps`.
* `forward(steps)` → Move forward by at most `steps`.

Example

```text
visit("google.com")
visit("facebook.com")
visit("youtube.com")

back(1)      → facebook.com
back(1)      → google.com
forward(1)   → facebook.com
visit("linkedin.com")
forward(2)   → linkedin.com
back(2)      → google.com
```

---

# Brute Force

## Idea

Maintain a list of visited pages and a pointer pointing to the current page.

* Visiting a new page:

  * Remove all forward history.
  * Append the new page.
* Back:

  * Move the pointer left.
* Forward:

  * Move the pointer right.

---

## Brute Force Code

```python
class BrowserHistory:

    def __init__(self, homepage):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url):

        self.history = self.history[:self.curr + 1]
        self.history.append(url)
        self.curr += 1

    def back(self, steps):

        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps):

        self.curr = min(len(self.history) - 1,
                        self.curr + steps)
        return self.history[self.curr]
```

---

## Complexity

| Operation | Complexity |
| --------- | ---------- |
| visit     | **O(n)**   |
| back      | **O(1)**   |
| forward   | **O(1)**   |

### Why is it slow?

Every time a new page is visited after going back,

```python
history = history[:curr+1]
```

creates a **new list**.

This copying makes `visit()` **O(n)**.

---

# Pattern

```text
Two Stacks Simulation
```

---

# Main Idea

Instead of copying the history list,

maintain two stacks.

```text
History Stack
```

stores

```text
Current page + Previous pages
```

```text
Future Stack
```

stores

```text
Pages removed using Back()
```

Operations become simple stack operations.

---

# Optimal Solution

```python
class BrowserHistory:

    def __init__(self, homepage):
        self.history = [homepage]
        self.future = []

    def visit(self, url):

        self.history.append(url)

        # New page removes forward history
        self.future = []

    def back(self, steps):

        while steps > 0 and len(self.history) > 1:

            self.future.append(
                self.history.pop()
            )

            steps -= 1

        return self.history[-1]

    def forward(self, steps):

        while steps > 0 and self.future:

            self.history.append(
                self.future.pop()
            )

            steps -= 1

        return self.history[-1]
```

---

# Why This Works

## History Stack

Contains

```text
Homepage

↓

Visited Pages

↓

Current Page
```

Example

```text
google

facebook

youtube
```

Current page

```text
youtube
```

---

## Future Stack

Stores pages removed by

```text
Back()
```

Example

After

```text
back(2)
```

History

```text
google
```

Future

```text
youtube

facebook
```

Top

```text
facebook
```

is the next page that can be restored.

---

# Why Clear Future on Visit?

Suppose

```text
google

↓

facebook

↓

youtube
```

Current page

```text
youtube
```

Now

```text
back(1)
```

History

```text
google

facebook
```

Future

```text
youtube
```

Now user visits

```text
linkedin
```

The browser creates

```text
google

facebook

linkedin
```

Can we still go forward to

```text
youtube
```

No.

Because a new browsing path has started.

Therefore,

```python
self.future = []
```

is mandatory.

---

# Dry Run

Operations

```text
visit(google)
visit(facebook)
visit(youtube)
```

History

```text
google

facebook

youtube
```

Future

```text
Empty
```

---

```text
back(1)
```

History

```text
google

facebook
```

Future

```text
youtube
```

Return

```text
facebook
```

---

```text
forward(1)
```

History

```text
google

facebook

youtube
```

Future

```text
Empty
```

Return

```text
youtube
```

---

```text
visit(linkedin)
```

History

```text
google

facebook

youtube

linkedin
```

Future

```text
Empty
```

---

# Common Mistakes

### 1. Forgetting to clear future

Always do

```python
self.future = []
```

after

```python
visit()
```

---

### 2. Popping homepage

History should always contain at least one page.

Correct

```python
while len(history) > 1
```

---

### 3. Forgetting `steps > 0`

Always stop after moving the required number of steps.

---

### 4. Using Queue instead of Stack

Browser history follows

```text
Last In

↓

First Out
```

Hence,

Stacks are the correct data structure.

---

# Complexity Comparison

| Operation | Brute Force | Two Stacks |
| --------- | ----------- | ---------- |
| visit     | O(n)        | O(1)       |
| back      | O(1)        | O(k)       |
| forward   | O(1)        | O(k)       |
| Space     | O(n)        | O(n)       |

> Here, `k` is the number of steps moved.

---

# Pattern Recognition

Use this pattern when:

* Undo / Redo operations
* Browser navigation
* Editor history
* Navigation history
* Forward / Back tracking

Similar Problems

* Browser History
* Undo Redo Editor
* Text Editor
* Navigation History

---

# Revision Cheat Sheet

```text
Pattern:
Two Stacks Simulation

History Stack:
Current page + previous pages

Future Stack:
Pages removed using Back()

visit():
Push into history
Clear future

back():
History → Future

forward():
Future → History

Remember:
✔ Clear future after visit()
✔ Never remove homepage
✔ Two stacks simulate browser navigation

Time:
visit → O(1)
back → O(k)
forward → O(k)

Space:
O(n)
```
