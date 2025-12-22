class Solution:
    def fib(self, n: int) -> int:
        """
        Computes the nth Fibonacci number using
        Top-Down Dynamic Programming (Memoization).

        Fibonacci Definition:
        fib(0) = 0
        fib(1) = 1
        fib(n) = fib(n-1) + fib(n-2)
        """

        def solve(n, memo):
            # If result is already computed, return it from cache
            if n in memo:
                return memo[n]

            # Base cases
            if n <= 1:
                return n

            # Store the computed result to avoid recomputation
            memo[n] = solve(n - 1, memo) + solve(n - 2, memo)
            return memo[n]

        # Cache to store previously computed Fibonacci values
        memo = {}
        return solve(n, memo)

Time Complexity

O(n)
Each Fibonacci number from 0 to n is computed once and stored in the memo dictionary.

Space Complexity

O(n)

O(n) for the memoization dictionary

O(n) for the recursion call stack
