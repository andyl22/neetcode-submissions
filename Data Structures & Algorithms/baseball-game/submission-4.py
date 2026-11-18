class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for o in operations:
            match o:
                case "+":
                    s.append(s[-1]+ s[-2])
                case "D":
                    s.append(s[-1] * 2)
                case "C":
                    s.pop()
                case _:
                    s.append(int(o))
        
        return sum(s)