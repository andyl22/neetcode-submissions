class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range((len(nums)*2))]

        for i, v in enumerate(nums):
            res[i], res[i+len(nums)] = v, v
        
        return res