class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums) * 2)
        j = len(nums)
        for i in range(j):
            res[i] = nums[i]
            res[j+i] = nums[i]
        
        return res