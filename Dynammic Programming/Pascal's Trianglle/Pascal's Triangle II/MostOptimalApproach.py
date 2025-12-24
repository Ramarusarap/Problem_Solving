def getRow(rowIndex):
    row = [1] * (rowIndex + 1)

    for k in range(1, rowIndex):
        row[k] = row[k - 1] * (rowIndex - k + 1) // k

    return row


Dry run:
| k | Formula      | Value | Row                  |
| - | ------------ | ----- | -------------------- |
| 1 | 1 × (5) / 1  | 5     | [1, 5, 1, 1, 1, 1]   |
| 2 | 5 × (4) / 2  | 10    | [1, 5, 10, 1, 1, 1]  |
| 3 | 10 × (3) / 3 | 10    | [1, 5, 10, 10, 1, 1] |
| 4 | 10 × (2) / 4 | 5     | [1, 5, 10, 10, 5, 1] |


Edge Cases
✅ rowIndex = 0
Output: [1]
Loop does not run.

✅ rowIndex = 1
Output: [1, 1]
Loop does not run.

✅ Large rowIndex
No factorials → no overflow
Python handles big integers safely
Loop runs n−1 times
