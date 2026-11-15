class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        i = 0
        res = []
        nums.sort()

        while i < len(nums)-3:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j = i + 1
            while j < len(nums)-2:
                if j -1 > i and nums[j] == nums[j-1]:
                    j += 1
                    continue
                l = j+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                j += 1
            i += 1
        return res