class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(end, start, nums):
            # next1 -> dp[i+1], next2 -> dp[i+2]
            next1 = 0
            next2 = 0

            # Iterate from 'start' down to 'end'
            # NOTE: range(start, end-1, -1) runs only if start >= end
            for i in range(start, end - 1, -1):
                # Option 1: rob current house -> nums[i] + next2
                # Option 2: skip current house -> next1
                curr = max(nums[i] + next2, next1)

                # Shift DP states
                next2 = next1
                next1 = curr

            # next1 stores the maximum loot for this range
            return next1

        # Edge case: only one house
        if len(nums) == 1:
            return nums[0]
        else:
            # Case 1: consider houses from index 0 to n-2
            # Case 2: consider houses from index 1 to n-1
            return max(
                solve(0, len(nums) - 2, nums),
                solve(1, len(nums) - 1, nums)
            )



Time Complexity: O(n)

The helper solve runs a single loop over a range of indices.
It is called twice (two cases for the circular constraint).
2 × O(n) → O(n).

Space Complexity: O(1)

Uses a constant number of variables (next1, next2, curr).
No extra arrays or recursion stack.
Input array is not modified.
