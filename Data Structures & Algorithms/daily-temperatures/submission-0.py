class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        results = [0 for _ in range(len(temperatures))]

        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                t = stack.pop()
                results[t] = i - t
            stack.append(i)
        
        return results