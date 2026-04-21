class Solution:
    # We know fibonacci is always 1,1,etc.
    # base case is n = 2, always return 1
    # else calculate from the base
    # memoize so we don't recalculate
    # same reference to the memo dict, so after all the recursive calls in the first "n-1" recursion, we should have some values
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

