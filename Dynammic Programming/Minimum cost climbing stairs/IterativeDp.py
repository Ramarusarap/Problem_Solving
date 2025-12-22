class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Computes the minimum cost to reach the top of the staircase
        without modifying the input array.

        Uses Bottom-Up Dynamic Programming with constant space.
        """

        n = len(cost)

        # dp0 -> min cost to reach step i-2
        # dp1 -> min cost to reach step i-1
        dp0, dp1 = 0, 0

        for i in range(2, n + 1):
            curr = min(dp1 + cost[i - 1], dp0 + cost[i - 2])
            dp0 = dp1
            dp1 = curr

        return dp1


Time Complexity

O(n)
Single pass through the array
Space Complexity

O(1)
Uses only three variables (dp0, dp1, curr)
No recursion, no extra arrays
