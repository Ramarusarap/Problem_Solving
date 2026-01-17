from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Returns the element that appears exactly once in the array,
        where every other element appears twice.

        Approach:
        - Use bitwise XOR to cancel out duplicate numbers.
        - XOR properties:
            1. a ^ a = 0
            2. a ^ 0 = a
            3. XOR is commutative and associative

        Time Complexity:
        - O(n), where n is the number of elements in nums.
          (Single pass through the array)

        Space Complexity:
        - O(1)
          (Constant extra space, no auxiliary data structures)
        """

        ans = 0  # Initialize accumulator (neutral element for XOR)

        for num in nums:          # O(n)
            ans ^= num            # XOR cancels duplicate values

        return ans                # Final remaining value
