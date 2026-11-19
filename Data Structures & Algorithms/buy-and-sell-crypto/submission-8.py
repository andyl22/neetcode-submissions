class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        best = 0
        smallest = 1000

        for p in prices:
            smallest = min(smallest, p)
            best = max(best, p - smallest)
        
        return best
