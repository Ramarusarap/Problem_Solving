class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Computes the number of distinct ways to climb to the top.
        At each step, you can climb either 1 or 2 stairs.

        This solution uses Top-Down Dynamic Programming (Memoization).
        """

        def solve(n, steptracker):
            # If already computed, return cached result
            if n in steptracker:
                return steptracker[n]

            # Base cases
            if n == 1 or n == 2:
                return n

            # Recurrence relation
            steptracker[n] = solve(n - 1, steptracker) + solve(n - 2, steptracker)
            return steptracker[n]

        # Dictionary to store results of subproblems
        steptracker = {}
        return solve(n, steptracker)

Time Complexity

O(n)

Why:
There are only n distinct subproblems (1 to n)
Each value is computed once
All repeated calls are returned in O(1) from the memo dictionary

Space Complexity

O(n)
Why:
O(n) for the memoization dictionary (steptracker)
O(n) for the recursion call stack in the worst case
