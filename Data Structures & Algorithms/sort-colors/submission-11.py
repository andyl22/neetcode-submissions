class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        i = 0
        r = len(nums)-1

        while i <= r:
            v = nums[i]
            if v == 0:
                nums[l], nums[i] = v, nums[l]
                l += 1
                i += 1
            elif v == 1:
                i += 1
            elif v == 2:
                nums[r], nums[i] = v, nums[r]
                r -= 1