class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float('inf')
        rollingSum = 0

        i = 0
        j = 0

        while j < len(nums):
            rollingSum += nums[j]
            while rollingSum >= target:
                if rollingSum >= target:
                    best = min(best, j - i + 1)
                rollingSum -= nums[i]
                i += 1
            j += 1

        return best if best != float('inf') else 0