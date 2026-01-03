import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Determines whether n is a power of two using logarithms.

        Mathematical Basis:
        A number n is a power of two if and only if log2(n) is an integer.

        Due to floating-point precision errors, we cannot directly check
        whether log2(n) is an integer. Instead, we check whether the computed
        value is sufficiently close to its nearest integer.
        """

        # Powers of two must be positive
        if n <= 0:
            return False

        # Compute log base 2 of n
        log_value = math.log(n, 2)

        # Check if log_value is close to an integer (tolerance-based comparison)
        return abs(log_value - round(log_value)) < 1e-10
