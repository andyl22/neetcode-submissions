class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = len(nums)-1
                while left < right:
                    t = nums[i] + nums[j] + nums[left] + nums[right]
                    prev = None
                    if t == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        prev = nums[left]
                        while nums[left] == prev and left != right:
                            left += 1
                    elif t > target:
                        prev = nums[right]
                        while nums[right] == prev and left != right:
                            right -= 1
                    else:
                        prev = nums[left]
                        while nums[left] == prev and left != right:
                            left += 1

        return res