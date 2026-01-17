from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Returns the element that appears more than ⌊n/2⌋ times.

        Approach: Boyer–Moore Voting Algorithm

        Time Complexity:
        - O(n) : Single pass through the array

        Space Complexity:
        - O(1) : Constant extra space
        """

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
