class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
        Calculates the total time a character remains poisoned.

        Each attack at time t poisons the character for `duration` seconds.
        If attacks occur before the previous poison wears off, the durations overlap
        and should not be double-counted.
        """

        total = 0

        # Sum the effective poison time contributed by each consecutive attack
        for i in range(len(timeSeries) - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)

        # Add poison duration from the last attack
        return total + duration

Time Complexity: O(n)
Space Complexity: O(1)
