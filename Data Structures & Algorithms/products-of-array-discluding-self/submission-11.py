class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1 for _ in range(len(nums))]
        postfixes = [1 for _ in range(len(nums))]

        prefix = 1
        for i in range(len(nums)):
            prefixes[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            postfixes[i] *= postfix
            postfix *= nums[i]
        
        for i in range(len(prefixes)):
            prefixes[i] = prefixes[i] * postfixes[i]
        return prefixes