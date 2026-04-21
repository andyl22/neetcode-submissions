class StockSpanner:

    def __init__(self):
        self.priceHistory = []

    def next(self, price: int) -> int:
        temp = [] + self.priceHistory
        self.priceHistory.append(price)
        
        res = 1
        while temp:
            cur = temp.pop()
            if cur <= price:
                res += 1
            else:
                break       
        return res

    # 100
    # 80, [100]
    # 60, [100, 80]
    # 70, [100, 80, 60]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)