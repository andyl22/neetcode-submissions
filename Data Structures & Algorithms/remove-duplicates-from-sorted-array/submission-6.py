class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        l = 0

        for i in range(len(nums)):
            if nums[i] != nums[l]:
                l += 1
                nums[l] = nums[i]

        return l+1