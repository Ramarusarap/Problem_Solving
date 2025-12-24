from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def helper(r: int, c: int) -> int:
            # Use symmetry to reduce computation
            c = min(c, r - c)
            res = 1
            for i in range(1, c + 1):
                res = res * (r - i + 1) // i
            return res

        ans = []
        for i in range(rowIndex + 1):
            # Reuse symmetry from already computed values
            if i > rowIndex // 2:
                ans.append(ans[rowIndex - i])
            else:
                ans.append(helper(rowIndex, i))

        return ans

⏱️ Complexity 

Time: O(n)  """ the inner for loop runs ≈ n² / 8 times in total. """
Space: O(rowIndex) (output only) 
