class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If I buy a stock, is there a price in the future where I can make a profit
        # Is there a price in the future where I haven't bought stock, but was still able to make a profit? (Signals a valley in stock price)
        memo = {}

        def rec(i, stock_owned):
            # base case
            if i == len(prices):
                return 0
            
            if (i,stock_owned) in memo:
                return memo[i,stock_owned]
            
            # do nothing
            res = rec(i+1, stock_owned)

            if stock_owned:
                res = max(res, prices[i] + rec(i+1,False))
            else:
                res = max(res, -prices[i] + rec(i+1,True))
            memo[(i,stock_owned)] = res
            return res
        return rec(0,False)