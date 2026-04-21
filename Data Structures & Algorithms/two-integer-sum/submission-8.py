class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = {}

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in r:
                return [r[remainder], i]
            r[nums[i]] = i