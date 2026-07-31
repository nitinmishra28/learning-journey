# 735. Asteroid Collision

## Problem

We are given an array of integers representing asteroids.

* Positive value → asteroid moves **right**.
* Negative value → asteroid moves **left**.
* The absolute value represents the asteroid's size.

When two asteroids moving in opposite directions collide:

* Smaller asteroid explodes.
* If both have the same size, both explode.
* Asteroids moving in the same direction never collide.

Return the state of the asteroids after all collisions.

### Examples

```text
Input : [5,10,-5]
Output: [5,10]
```

```text
Input : [8,-8]
Output: []
```

```text
Input : [10,2,-5]
Output: [10]
```

---

# Brute Force

## Idea

Keep scanning the array.

Whenever two adjacent asteroids can collide:

* Resolve the collision.
* Create a new array.
* Repeat until no collision is possible.

---

## Brute Force Code

```python
class Solution:
    def asteroidCollision(self, asteroids):

        changed = True

        while changed:
            changed = False
            result = []

            i = 0

            while i < len(asteroids):

                if (
                    i < len(asteroids) - 1
                    and asteroids[i] > 0
                    and asteroids[i + 1] < 0
                ):

                    changed = True

                    left = asteroids[i]
                    right = asteroids[i + 1]

                    if abs(left) > abs(right):
                        result.append(left)

                    elif abs(left) < abs(right):
                        result.append(right)

                    # Equal size → both destroyed

                    i += 2

                else:
                    result.append(asteroids[i])
                    i += 1

            asteroids = result

        return asteroids
```

---

## Complexity

* **Time:** `O(n²)`
* **Space:** `O(n)`

### Why is it slow?

After every collision,

the array is rebuilt,

and the entire array is scanned again.

---

# Pattern

```text
Stack + Collision Simulation
```

---

# Main Idea

Maintain a stack of asteroids that have survived so far.

A collision is only possible when

```text
Top of Stack → Positive

Current Asteroid → Negative
```

because they are moving towards each other.

For every collision:

* Larger asteroid survives.
* Smaller asteroid is destroyed.
* Equal size → both are destroyed.

The stack automatically keeps only the surviving asteroids.

---

# Optimal Solution

```python
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:

            while stack and stack[-1] > 0 and asteroid < 0:

                # Current asteroid is larger
                if -asteroid > stack[-1]:
                    stack.pop()
                    continue

                # Both are equal
                elif stack[-1] == -asteroid:
                    stack.pop()
                    break

                # Stack asteroid is larger
                else:
                    break

            else:
                stack.append(asteroid)

        return stack
```

---

# Why Collision Happens Only in One Case

Many beginners think every positive and negative asteroid can collide.

That's incorrect.

Collision is possible **only when**

```text
Stack Top  →  +

Current    →  -
```

Example

```text
5   -3

→ ←
```

Both move towards each other.

Collision occurs.

---

These cases never collide.

```text
-5   3

← →
```

Moving away from each other.

---

```text
5   3

→ →
```

Same direction.

---

```text
-5  -3

← ←
```

Same direction.

Therefore, the collision condition is

```python
while stack and stack[-1] > 0 and asteroid < 0:
```

This single condition solves the entire problem.
