# Minimum Path Sum (In-Place DP)

## Problem
Given an `m x n` grid filled with non-negative numbers, find a path from
the top-left to the bottom-right that minimizes the sum of all numbers
along the path.

Allowed moves:
- Right
- Down

---

## Optimal Approach

This solution uses **bottom-up dynamic programming** and updates the
input grid **in place**.


---

## Complexity Analysis

- **Time Complexity:** `O(m × n)`
- **Extra Space Complexity:** `O(1)` (grid reused)

---

## Why Not Recursion?

- Adds call stack overhead
- Risk of recursion depth limits
- Uses more space without benefit
- Iterative DP is simpler and more robust

---

## Interview One-Liner

> I solve it using bottom-up dynamic programming and reuse the grid itself to achieve O(1) extra space.

---

## Notes
- Input grid is modified in place
- This is the most efficient and interview-preferred solution
