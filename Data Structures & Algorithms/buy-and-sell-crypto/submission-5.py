class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 100
        best = 0

        for p in prices:
            lowest = min(lowest,p)
            profit = p - lowest
            best = max(best, profit)

        return best