class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores=[]

        for o in operations:
            match o:
                case "+":
                    scores.append(scores[-1] + scores[-2])
                case "D":
                    scores.append(scores[-1]*2)
                case "C":
                    scores.pop()
                case _:
                    scores.append(int(o))
        
        return sum(scores)