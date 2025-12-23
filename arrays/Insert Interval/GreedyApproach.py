class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Inserts a new interval into a list of non-overlapping intervals
        and merges if necessary.

        Approach:
        - Add the new interval to the list
        - Sort intervals by start time
        - Merge overlapping intervals using a linear scan
        """

        # Add the new interval to the existing list
        intervals.append(newInterval)

        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])

        result = []

        # Edge case: no intervals
        if len(intervals) == 0:
            result.append([])
            return result

        # Edge case: only one interval
        elif len(intervals) == 1:
            result.append(intervals[0])
            return result

        # Initialize the first interval
        x, y = intervals[0]

        # Traverse remaining intervals
        for i in range(1, len(intervals)):
            # If current interval overlaps with [x, y], merge them
            if intervals[i][0] <= y:
                y = max(y, intervals[i][1])
            else:
                # No overlap, push the current merged interval
                result.append([x, y])
                x, y = intervals[i]

            # Debug print to observe current merge state
            print([x, y])

        # Append the last merged interval
        result.append([x, y])

        return result

Time Complexity

O(n log n)
Sorting dominates the runtime.
Single linear scan afterward.

Space Complexity

O(n)
Result list stores merged intervals.
