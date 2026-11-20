class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for n in nums:
            if n-1 in nums:
                continue
            else:
                count = 1
                while n + 1 in nums:
                    count += 1
                    n += 1
                best = max(best, count)
        return best