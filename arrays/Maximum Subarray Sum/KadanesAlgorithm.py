class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of a contiguous subarray
        using Kadane's Algorithm.
        """

        # curr_sum -> best subarray sum ending at current index
        # max_sum  -> best subarray sum seen so far
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            # Either extend the previous subarray or start new
            curr_sum = max(nums[i], curr_sum + nums[i])

            # Update global maximum
            max_sum = max(max_sum, curr_sum)

        return max_sum


Kadane’s Algorithm finds the maximum sum of a contiguous (consecutive) subarray in O(n) time and O(1) space.
At each index, decide whether to extend the previous subarray or start a new one at the current element.

Why it works
1. If the running sum becomes worse than starting fresh, reset.
2. Otherwise, keep extending.
3. This local choice leads to the global optimum.
