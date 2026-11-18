class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if t not in "+-*/":
                s.append(int(t))
            else:
                s2 = s.pop()
                s1 = s.pop()
                match t:
                    case "+":
                        s.append(s1+s2)
                    case "-":
                        s.append(s1 - s2)
                    case "*":
                        s.append(s1 * s2)
                    case "/":
                        s.append(int(s1/s2))
        
        return s[0]