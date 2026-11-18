class StockSpanner:

    def __init__(self):
        self.m_span = []

    def next(self, price: int) -> int:
        res = 1
        while self.m_span:
            peek = self.m_span[-1]
            if price >= peek[0]:
                res += peek[1]
                self.m_span.pop()
            else:
                break
        self.m_span.append((price, res))
        return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)