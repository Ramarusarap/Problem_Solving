class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        LeetCode 904 – Fruit Into Baskets

        Approach:
        - Maintain at most two distinct fruits in a sliding window.
        - Track the length of the current valid subarray.
        - Track the count of the last contiguous fruit to correctly
          shrink the window when a third fruit appears.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(fruits)
        if n <= 1:
            return n

        distinct = []          # stores the two fruit types in the window
        subarrayLength = 0     # current window length
        maxLength = 0          # maximum valid window length found
        lastCount = 0          # count of last contiguous fruit

        for i in range(n):

            # Case 1: first fruit
            if len(distinct) == 0:
                distinct.append(fruits[i])
                subarrayLength = 1
                lastCount = 1

            # Case 2: second distinct fruit
            elif len(distinct) < 2:
                if fruits[i] not in distinct:
                    distinct.append(fruits[i])
                    lastCount = 1
                else:
                    lastCount += 1
                subarrayLength += 1

            # Case 3: already two distinct fruits
            else:
                # If current fruit matches one of the two
                if fruits[i] in distinct:
                    subarrayLength += 1
                    if fruits[i] == fruits[i - 1]:
                        lastCount += 1
                    else:
                        lastCount = 1
                else:
                    # Third fruit encountered → shrink window
                    maxLength = max(maxLength, subarrayLength)

                    # Keep only the last contiguous fruit and current fruit
                    distinct = [fruits[i - 1], fruits[i]]
                    subarrayLength = lastCount + 1
                    lastCount = 1

        return max(maxLength, subarrayLength)
