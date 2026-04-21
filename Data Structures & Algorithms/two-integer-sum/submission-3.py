class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, x in enumerate(nums):
            r = target - x
            if r in diffs:
                return [diffs[r], i]
            elif x in diffs:
                return
            else:
                diffs[x] = i
        