class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rMap = {}

        for i, n in enumerate(nums):
            r = target - n
            if r in rMap:
                return [rMap[r], i]
            rMap[n] = i