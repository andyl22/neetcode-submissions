class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rMap = {}

        for i in range(len(nums)):
            if nums[i] in rMap:
                return [rMap[nums[i]], i]
            r = target - nums[i]
            rMap[r] = i