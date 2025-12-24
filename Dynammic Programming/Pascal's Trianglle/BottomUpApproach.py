class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generates the first `numRows` of Pascal's Triangle.

        Each element is the sum of the two elements directly above it
        from the previous row.
        """

        # Initialize with a dummy empty row to simplify indexing
        triangle = [[]]

        for i in range(1, numRows + 1):
            row = []
            for j in range(i):
                # First and last elements of each row are always 1
                if j == 0 or j == i - 1:
                    row.append(1)
                else:
                    # Sum of two elements from the previous row
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

            triangle.append(row)

        # Remove the initial dummy row
        return triangle[1:]

⏱ Time Complexity

O(n²)
Total elements generated = 1 + 2 + ... + n = O(n²)

🧠 Space Complexity

O(n²)
Stores all rows of Pascal’s Triangle.

"""If you don’t want to use a dummy first row, then you must change the indexing contract.
You cannot keep the same indexing and just remove the dummy"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generates the first `numRows` of Pascal's Triangle
        without using a dummy row.
        """

        if numRows == 0:
            return []

        ans = []

        for i in range(numRows):
            row = []
            for j in range(i + 1):
                # First and last elements of each row are always 1
                if j == 0 or j == i:
                    row.append(1)
                else:
                    # Access previous row using i - 1
                    row.append(ans[i - 1][j - 1] + ans[i - 1][j])

            ans.append(row)

        return ans
