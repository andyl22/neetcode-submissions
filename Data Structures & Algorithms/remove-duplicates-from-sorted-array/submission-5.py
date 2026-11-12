class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        l = 0

        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[l] = nums[i]
                l += 1
            seen.add(nums[i])

        
        return l