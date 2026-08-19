class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        s = []

        for i in range(len(temperatures)):
            while len(s) and temperatures[s[-1]] < temperatures[i]:
                prevIndex = s.pop()
                res[prevIndex] = i - prevIndex
            s.append(i)
            
        return res