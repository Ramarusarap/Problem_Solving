class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        Returns the maximum count between negative and positive numbers
        in a sorted array.

        Time Complexity: O(log n)
        - Two binary searches are performed.
        - Each binary search runs in O(log n).

        Space Complexity: O(1)
        - Only constant extra variables are used.
        """

        n = len(nums)

        # -------- Count negative numbers --------
        # Find the first index where nums[i] >= 0
        # All elements before this index are negative
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2  # O(1)
            if nums[mid] < 0:
                left = mid + 1        # discard left half
            else:
                right = mid           # discard right half

        # Number of negative elements
        neg = left

        # -------- Count positive numbers --------
        # Find the first index where nums[i] > 0
        # All elements from this index to end are positive
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2  # O(1)
            if nums[mid] <= 0:
                left = mid + 1        # skip non-positive values
            else:
                right = mid           # potential first positive

        # Number of positive elements
        pos = n - left

        # Return the maximum of positive and negative counts
        return max(neg, pos)
