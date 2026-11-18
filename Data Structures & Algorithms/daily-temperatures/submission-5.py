class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                temperatures[j] = i - j
            stack.append(i)

        while stack:
            temperatures[stack.pop()] = 0
        return temperatures
            

