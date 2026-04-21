class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        lowest = 100000000

        for i in range(len(prices)):
            lowest = min(lowest, prices[i])
            best = max(best, prices[i] - lowest)

        return best
