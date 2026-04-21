class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(self.climb(cost, 0, memo), self.climb(cost, 1, memo))
        

    def climb(self, cost, n, memo):
        if n >= len(cost):
            return 0
        if n in memo:
            return memo[n]
        
        

        memo[n] = cost[n] + min(self.climb(cost, n+1, memo),  self.climb(cost, n+2, memo))
        return memo[n]