class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nLen = len(nums)
        ans = [0 for _ in range(nLen*2)]
        for i,v in enumerate(nums):
            ans[i] = v
            ans[i+nLen] = v
        
        return ans