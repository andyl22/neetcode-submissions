class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # never take a loss
        # no point of selling until we hit the high point in a subset
        # peek to the future value
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit