class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        out = 0
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                match t:
                    case "+":
                        stack.append(n1+n2)
                    case "-":
                        stack.append(n2-n1)
                    case "*":
                        stack.append(n2*n1)
                    case "/":
                        stack.append(int(n2/n1))
        
        return stack[0]