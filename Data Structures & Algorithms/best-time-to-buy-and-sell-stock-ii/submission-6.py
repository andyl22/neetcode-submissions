class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rollingSum = 0

        for i in range(1, len(prices), 1):
            if prices[i-1] < prices[i]:
                rollingSum += prices[i] - prices[i-1]
        return rollingSum