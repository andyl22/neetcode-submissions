class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def rec(i, state_variable):
            if i > len(prices)-1:
                return 0
            if (i,state_variable) in memo:
                return memo[i,state_variable]
            
            res = rec(i+1,state_variable)

            if state_variable == True:
                res = max(res, prices[i] + rec(i+1,False))
            else:
                res = max(res, -prices[i] + rec(i+1,True))
            memo[(i,state_variable)] = res
            return res
            
        return rec(0,False)