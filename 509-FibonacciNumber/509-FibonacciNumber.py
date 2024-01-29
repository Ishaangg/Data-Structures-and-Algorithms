class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)
        if n == 0:
            return 0
        if n == 1:
            return 1

        if dp[n] != -1:
            return dp[n]

        val = self.fib(n - 1) + self.fib(n - 2)

        dp[n] = val  

        return val


2
