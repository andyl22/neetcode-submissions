class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r)//2
            mNum = nums[mid]
            if mNum == target:
                return mid
            elif mNum > target:
                r = mid - 1
            else:
                l = mid + 1

        return l