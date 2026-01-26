from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Counts the number of subarrays consisting only of zeros.

        Optimal Approach:
        - Maintain a running count of consecutive zeros.
        - For every zero encountered, add the current count to result.
        - Reset count when a non-zero appears.

        Example:
        nums = [0, 0, 0]
        count progression = 1, 2, 3
        result = 1 + 2 + 3 = 6

        Time Complexity:
        - O(n)

        Space Complexity:
        - O(1)
        """

        result = 0
        count = 0

        for num in nums:
            if num == 0:
                count += 1
                result += count
            else:
                count = 0

        return result
