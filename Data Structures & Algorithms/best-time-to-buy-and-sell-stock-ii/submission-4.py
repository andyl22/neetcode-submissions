class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rollingProfit = 0
        prev = 30000

        for p in prices:
            if p > prev:
                rollingProfit += p - prev
                prev = p
            prev = min(p, prev)
        
        return rollingProfit