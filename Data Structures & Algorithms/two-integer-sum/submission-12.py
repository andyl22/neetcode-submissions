class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rMap = {}

        for i, v in enumerate(nums):
            remainder = target - v
            if remainder in rMap:
                return [rMap[remainder], i]
            rMap[v] = i