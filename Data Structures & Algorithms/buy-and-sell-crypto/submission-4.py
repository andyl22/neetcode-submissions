class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 100
        best = 0

        for p in prices:
            lowest = min(p, lowest)
            best = max(p-lowest, best)
        
        return best
