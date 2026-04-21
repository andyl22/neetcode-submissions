class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # never take a loss
        # no point of selling until we hit the high point in a subset
        # peek to the future value
        profit = 0
        high = prices[0]
        low = prices[0]

        for i in range(len(prices)):
            if prices[i] >= high:
                high = prices[i]

            if prices[i] < high or i == len(prices)-1:
                profit += high - low
                low = prices[i]
                high = prices[i]

        return profit