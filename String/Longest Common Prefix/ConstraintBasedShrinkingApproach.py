from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix among a list of strings.

        Approach (Length-based shrinking prefix):
        1. Sort strings by length so the shortest string bounds the prefix.
        2. Start with the full length of the shortest string as the prefix length.
        3. For each string, shrink the prefix length until it matches.
        4. Return the remaining prefix.

        Time Complexity:
        - O(n log n) due to sorting
        - O(n * m) for prefix comparison
        - Overall: O(n log n + n * m)

        Space Complexity:
        - O(1) extra space (in-place sort, constant variables)

        Notes / Criticisms Addressed:
        - Handles empty input safely
        - Prevents infinite loop by checking prefix_len > 0
        - Avoids unnecessary comparisons once prefix length becomes zero
        - Uses slicing carefully and intentionally
        """

        # Edge case: empty list of strings
        if not strs:
            return ""

        # Sort by string length so the shortest string limits the prefix
        strs.sort(key=len)

        # Maximum possible prefix length is the length of the shortest string
        prefix_len = len(strs[0])

        # Compare prefix with each remaining string
        for s in strs[1:]:
            # Shrink prefix length until it matches the current string
            while prefix_len > 0 and s[:prefix_len] != strs[0][:prefix_len]:
                prefix_len -= 1

            # Early exit: no common prefix exists
            if prefix_len == 0:
                return ""

        # Return the final valid prefix
        return strs[0][:prefix_len]
