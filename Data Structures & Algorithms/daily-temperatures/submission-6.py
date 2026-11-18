class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # Stores indices

        for i, t in enumerate(temperatures):
            # While stack top is colder than today's temperature
            while stack and temperatures[stack[-1]] < t:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            
            stack.append(i)

        return res