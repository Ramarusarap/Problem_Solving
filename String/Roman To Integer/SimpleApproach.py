from typing import Dict

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral to an integer.

        Approach:
        - Traverse the string from right to left.
        - If the current numeral is smaller than the numeral to its right,
          subtract its value; otherwise, add it.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        roman_map: Dict[str, int] = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s) - 1, -1, -1):
            # Subtract if a smaller value precedes a larger value
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]

        return total

Time Complexity: `O(n)`
Space Complexity: `O(1)`
Where `n` is the length of the Roman numeral string.
