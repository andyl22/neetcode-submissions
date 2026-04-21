class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 101
        best = 0

        for p in prices:
            low = min(p, low)
            best = max(best, p - low)
        
        return best