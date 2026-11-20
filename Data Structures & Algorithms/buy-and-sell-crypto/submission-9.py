class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        lowest = float('inf')

        for p in prices:
            best = max(best, p - lowest)
            lowest = min(lowest, p)

        return best