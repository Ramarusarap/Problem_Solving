from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Compute the number of unique paths in an m x n grid using
        space-optimized bottom-up dynamic programming.

        The robot can only move right or down.

        Time Complexity: O(m * n)
        Space Complexity: O(n)
        """

        # 1D DP array where ans[j] represents number of ways
        # to reach column j in the current row
        ans = [1 for _ in range(n)]

        # Build DP row by row
        for _ in range(1, m):
            for j in range(1, n):
                ans[j] = ans[j] + ans[j - 1]

        return ans[n - 1]
