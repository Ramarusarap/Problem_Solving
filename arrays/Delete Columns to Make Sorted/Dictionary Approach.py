class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Dictionary to track the maximum ASCII value seen so far
        # for each column index
        tracker = {}

        # Traverse each string row by row
        for row, s in enumerate(strs):
            # Traverse each character column-wise
            for ix, c in enumerate(s):
                # Initialize tracker using the first row
                if row == 0:
                    tracker[ix] = ord(c)
                else:
                    # If current character maintains non-decreasing order
                    # update the maximum ASCII value for that column
                    if ord(c) >= tracker[ix]:
                        tracker[ix] = ord(c)
                    else:
                        # Mark this column as invalid using a sentinel value
                        # since it violates sorted order
                        tracker[ix] = 1000

        # Count how many columns were marked invalid
        count = 0
        for i in tracker:
            if tracker[i] == 1000:
                count += 1

        return count

Time Complexity: O(n × m)
Space Complexity: O(m)

where n is the number of strings and m is the length of each string.
