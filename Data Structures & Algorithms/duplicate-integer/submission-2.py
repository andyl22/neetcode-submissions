class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for x in nums:
            if x in seen:
                return True
            else:
                seen[x] = 1
        return False
         