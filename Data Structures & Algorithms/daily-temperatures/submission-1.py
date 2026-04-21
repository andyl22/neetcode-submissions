class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i,v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                p = stack.pop()
                d = i-p[1]
                result[p[1]] = d
            stack.append((v,i))
        
        return result