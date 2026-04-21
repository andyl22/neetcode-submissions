class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # we need to iterate over the array, each additional step having 2 possible outcomes
        # recursion to explore both paths
        # we want to do a comparison on which is cheaper and then add it to the sum
        memo = {}
        return min(self.iterate(cost, 0, memo), self.iterate(cost,1, memo))

    def iterate(self, cost, n, memo):
        if n >= len(cost):
            return 0
        if n in memo:
            return memo[n]
        
        price1 = self.iterate(cost, n+1, memo)
        price2 = self.iterate(cost, n+2, memo)
        memo[n] = cost[n] + min(price1, price2)
        return memo[n]
        