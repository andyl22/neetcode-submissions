class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        j = 0
        r = len(nums)-1

        while j <= r:
            v = nums[j]
            if v == 1:
                j += 1
            elif v == 0:
                nums[l], nums[j] = v, nums[l]
                j += 1
                l += 1
            else:
                nums[r], nums[j] = v, nums[r]
                r -= 1
        

                