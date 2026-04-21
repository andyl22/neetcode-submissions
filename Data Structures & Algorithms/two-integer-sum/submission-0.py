class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(nums):
            t = target - n
            if t in s:
                return [s[t], i]
            s[n] = i
