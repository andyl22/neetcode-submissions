class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o not in "+DC":
                stack.append(int(o))
            else:
                match o:
                    case "+":
                        stack.append(stack[-1] + stack[-2])
                    case "D":
                        stack.append(stack[-1] * 2)
                    case "C":
                        stack.pop()
        return sum(stack)