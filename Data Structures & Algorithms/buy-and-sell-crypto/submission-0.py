class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 1000000000000
        best = 0
        for price in prices:
            if price < lowest:
                lowest = price
            best = price - lowest if price -lowest > best else best
        return best
