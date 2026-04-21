class StockSpanner:

    def __init__(self):
        self.priceHistory = []

    def next(self, price: int) -> int:
        # self.priceHistory.append(price)
        
        res = 1
        while self.priceHistory:
            peek = self.priceHistory[-1]
            if price >= peek[0]:
                res += peek[1]
                self.priceHistory.pop()
            else:
                break

        self.priceHistory.append((price, res))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)