class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums)-1
        c = 0

        while c <= r:
            if nums[c] == 0:
                nums[l], nums[c] = nums[c], nums[l]
                c += 1
                l += 1
            elif nums[c] == 1:
                c += 1
            else:
                nums[c], nums[r] = nums[r], nums[c]
                r -= 1