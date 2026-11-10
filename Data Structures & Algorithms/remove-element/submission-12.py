class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)-1
        k = 0

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], val
                r -= 1
            else:
                l += 1
                k += 1

        return k