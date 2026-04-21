class MyQueue:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        temp = self.s[0]
        self.s = self.s[1:]
        return temp

    def peek(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        return False if len(self.s) else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()