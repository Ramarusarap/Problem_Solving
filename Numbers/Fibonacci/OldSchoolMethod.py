class Solution:
    def fib(self, n: int) -> int:
        """
        Computes the nth Fibonacci number using an iterative approach.

        Fibonacci Definition:
        fib(0) = 0
        fib(1) = 1
        fib(n) = fib(n-1) + fib(n-2)

        This solution uses constant space by maintaining only
        the previous two Fibonacci values.
        """

        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1

        # Initialize the first two Fibonacci numbers
        first, second = 0, 1

        # Start computing from fib(2) up to fib(n)
        i = 2
        while i <= n:
            # Update values atomically to preserve correctness
            first, second = second, first + second
            i += 1

        # 'second' holds fib(n) at the end of the loop
        return second


Time Complexity

O(n)
The loop runs once for each value from 2 to n.

Space Complexity

O(1)
Only two variables are used regardless of input size.
