class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Computes the minimum cost to reach the top of the staircase.
        You can start from step 0 or step 1, and at each step you can climb
        either 1 or 2 steps.

        This solution uses Bottom-Up Dynamic Programming and modifies
        the input array in place to achieve constant extra space.
        """

        # Append a dummy 0 to represent the top floor (no cost to stand on it)
        cost.append(0)

        # Process the array from right to left
        # Each cost[i] becomes the minimum cost to reach the top from step i
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])

        # You can start from step 0 or step 1
        return min(cost[0], cost[1])

Time Complexity

O(n)
The loop runs once over the array
Each iteration performs constant work

Space Complexity
O(1) (extra space)
No additional DP array is used
The input list is reused to store DP values

Why this solution is optimal
1. Eliminates recursion and stack usage
2. Avoids extra memory.
3. Guarantees no out-of-bounds access
4. Clean bottom-up DP implementation
