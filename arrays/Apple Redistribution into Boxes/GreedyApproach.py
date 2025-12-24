class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        """
        Determines the minimum number of boxes required to store all apples.

        Approach:
        - Calculate the total number of apples
        - Sort box capacities
        - Greedily use the largest capacity boxes first
        """

        # Calculate total number of apples
        total_apples = 0
        for i in range(len(apple)):
            total_apples += apple[i]

        # Sort capacities in ascending order
        capacity.sort()

        # Use boxes from largest to smallest capacity
        for i in range(len(capacity) - 1, -1, -1):
            # If current box can hold all remaining apples
            if total_apples - capacity[i] <= 0:
                break
            else:
                # Fill the box and reduce remaining apples
                total_apples -= capacity[i]

        # Number of boxes used
        return len(capacity) - i

⏱ Time Complexity

O(n + m log m)
n = number of apple piles
m = number of boxes

Sorting capacities dominates

🧠 Space Complexity
O(1) extra space
(sorting in place, no additional data structures)
