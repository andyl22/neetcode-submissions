class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = ["" for _ in range(l*2)]

        for i in range(l):
            ans[i] = nums[i]
            ans[l+i] = nums[i]
        
        return ans