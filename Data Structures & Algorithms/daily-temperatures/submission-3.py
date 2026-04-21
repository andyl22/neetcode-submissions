class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lenT= len(temperatures)
        stack = []
        res = [0 for _ in range(lenT)]

        for i in range(lenT):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                p = stack.pop()
                res[p] = i - p
            stack.append(i)
        
        return res
