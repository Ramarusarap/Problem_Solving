class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Determines whether n is a power of two using bit manipulation.

        Bitwise Insight:
        A power of two has exactly one set bit in its binary representation.

        The expression (n & (n - 1)) removes the lowest set bit of n.
        If n has only one set bit, the result becomes 0.
        """

        # Powers of two must be positive
        if n <= 0:
            return False

        # Check if n has exactly one set bit
        return (n & (n - 1)) == 0
