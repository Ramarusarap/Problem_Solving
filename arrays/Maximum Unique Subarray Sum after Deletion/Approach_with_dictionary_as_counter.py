class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Dictionary to track unique non-negative numbers
        posmarker = {}

        # To track the maximum negative number (edge case:
        # when all elements are negative)
        negmarker = -101   # constraint-based initialization

        # Traverse the array
        for i in nums:
            if i < 0:
                # Track the maximum negative number
                negmarker = max(negmarker, i)
            else:
                # Store unique non-negative numbers
                if i in posmarker:
                    posmarker[i] += 1
                else:
                    posmarker[i] = 1

        # If no non-negative numbers exist,
        # return the maximum negative number
        if len(posmarker) == 0:
            return negmarker
        else:
            # Sum of all unique non-negative values
            ans = 0
            for i in posmarker:
                ans += i
            return ans



Time Complexity: O(n)
Space Complexity: O(n) (for storing unique elements)
