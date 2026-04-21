class Solution:
    def f(self, n: int, memo):
        if n <= 2:
            return n
        if n in memo:
            return memo[n]
        
        # Recursive step with self
        memo[n] = self.f(n - 1, memo) + self.f(n - 2, memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        # Initialize the memo here so the caller doesn't have to
        return self.f(n, {})

