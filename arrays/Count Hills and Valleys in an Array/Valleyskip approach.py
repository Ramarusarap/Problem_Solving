class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        """
        A hill is a number strictly greater than its nearest different neighbors.
        A valley is a number strictly smaller than its nearest different neighbors.
        Consecutive equal values are ignored while determining neighbors.
        """

        n = len(nums)
        count = 0

        # Iterate through each possible middle element
        for i in range(1, n - 1):

            # Skip duplicate values to avoid counting the same plateau multiple times
            if nums[i] == nums[i - 1]:
                continue

            left = i - 1
            right = i + 1

            # Move left pointer to the nearest different value
            while left >= 0 and nums[left] == nums[i]:
                left -= 1

            # Move right pointer to the nearest different value
            while right < n and nums[right] == nums[i]:
                right += 1

            # Ensure both neighbors are within bounds
            if left >= 0 and right < n:
                # Check for hill
                if nums[i] > nums[left] and nums[i] > nums[right]:
                    count += 1
                # Check for valley
                elif nums[i] < nums[left] and nums[i] < nums[right]:
                    count += 1

        return count


Consecutive duplicates form plateaus and must be considered as a single value.
For each candidate index, we:
  Skip equal values on both sides
  Compare with the nearest distinct neighbors
A guard condition prevents double counting of plateaus.

⏱ Time Complexity

  O(n)

  Why?
      The main loop runs n times.
      Although there are inner while loops, each index is skipped at most once across the entire algorithm.
      This is an amortized O(n) two-pointer pattern.

💾 Space Complexity

  O(1)

  Only constant extra variables (left, right, count) are used.
  No auxiliary data structures.
