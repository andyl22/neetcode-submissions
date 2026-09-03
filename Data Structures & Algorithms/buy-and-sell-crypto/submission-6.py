class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = max(prices)
        best = 0

        for i in range(len(prices)):
            lowest = min(prices[i], lowest)
            profit = prices[i] - lowest
            best = max(profit, best)

        return best