class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0

        for n in nums:
            length = 0
            if n-1 in nums:
                continue
            else:
                while n+1 in nums:
                    length += 1
                    n += 1
            
            best = max(length+1,best)
        return best

