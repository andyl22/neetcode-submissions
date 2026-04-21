class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      prevMap = {}
      for i, c in enumerate(nums):
        remainder = target - c
        if remainder in prevMap:
          return [prevMap[remainder], i]
        prevMap[c] = i
