class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # Use nums[i] instead of v so it updates dynamically after every swap
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            
        for i,v in enumerate(nums):
            if i != v-1:
                return i+1
        
        return nums[len(nums)-1]+1