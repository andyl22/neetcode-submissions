class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            remainder = target - n
            if remainder in seen:
                return [seen[remainder], i]
            seen[n] = i
