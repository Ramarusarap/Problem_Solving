class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        """
        Given an array of size 2N where one element is repeated N times
        and all other elements appear exactly once, return the repeated element.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        n = len(nums) // 2      # N = half of the array size
        freq = {}              # Frequency map

        for num in nums:
            # Update frequency count
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            # Once frequency reaches N, return immediately
            if freq[num] == n:
                return num

        return -1  # Fallback (problem guarantees a valid answer)
