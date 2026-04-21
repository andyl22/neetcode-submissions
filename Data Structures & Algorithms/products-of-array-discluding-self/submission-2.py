class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            # get the left multiples
            # [1,2,3,4]
            # [1, 1*1, 1*2, 1*4]
            output[i] = nums[i-1] * output[i-1]
        
        # multiply the left multiples by the right
        # [1,1,2,4]
        # 
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output