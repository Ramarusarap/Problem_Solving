class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Find the earliest closing time that minimizes penalty.

        Idea:
        - Treat 'Y' as +1 (penalty saved if kept open)
        - Treat 'N' as -1 (penalty added if kept open)
        - Find the prefix with maximum cumulative savings
        - Closing time is index + 1 of that prefix

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        penaltySaved = 0
        maxSaved = 0
        when = 0

        for i in range(len(customers)):
            if customers[i] == 'Y':
                penaltySaved += 1
            else:
                penaltySaved -= 1

            # Update the best closing time when savings improve
            if penaltySaved > maxSaved:
                maxSaved = penaltySaved
                when = i + 1  # close AFTER hour i

        return when

Time: O(n)
Space: O(1)
