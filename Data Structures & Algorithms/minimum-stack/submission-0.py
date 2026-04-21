class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # If the stack is empty, the new value is the minimum.
        # Otherwise, compare val with the current minimum at the top of the stack.
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        # Return the value part of the tuple
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the pre-calculated minimum part of the tuple
        return self.stack[-1][1]