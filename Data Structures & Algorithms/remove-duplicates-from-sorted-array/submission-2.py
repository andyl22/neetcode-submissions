class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        seen = {}

        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[w] = nums[i]
                w += 1
            seen[nums[i]] = 1
        return w