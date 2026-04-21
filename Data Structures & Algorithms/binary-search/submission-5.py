class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        # 0, 1, 2;; target = 0 or 2
        # r = 2, l = 0;; mid = 1
        while l <= r:
            mid = (l + r) // 2
            midNum = nums[mid]
            if midNum == target:
                return mid
            elif midNum < target:
                l = mid+1
            else:
                r = mid-1
        
        return -1