class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-/*":
                stack.append(int(t))
            else:
                s1 = stack.pop()
                s2 = stack.pop()
                if t == "+":
                    stack.append(s2+s1)
                elif t == "-":
                    stack.append(s2-s1)
                elif t == "/":
                    stack.append(int(s2/s1))
                elif t == "*":
                    stack.append(s2*s1)


        return stack[-1]