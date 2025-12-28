class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all zeroes to the end of the array while maintaining
        the relative order of non-zero elements.

        Time Complexity: O(n)
        - The loop runs once over the array of size n.
        - Each element is processed exactly one time.

        Space Complexity: O(1)
        - The algorithm modifies the array in-place.
        - No extra data structures are used.
        """

        # Pointer i indicates the index where the next non-zero
        # element should be placed
        i = 0

        # Pointer j scans the array from left to right (O(n) traversal)
        for j in range(len(nums)):
            # If the current element is non-zero
            if nums[j] != 0:
                # Swap the non-zero element to index i
                # This operation is O(1)
                nums[i], nums[j] = nums[j], nums[i]

                # Move i forward to the next position
                i += 1
