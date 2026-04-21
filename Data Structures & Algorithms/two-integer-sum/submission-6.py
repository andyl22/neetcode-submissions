class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rMap = {}

        for i in range(len(nums)):
            r = target - nums[i]
            if r in rMap:
                return [rMap[r], i]
            rMap[nums[i]] = i