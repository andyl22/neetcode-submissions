class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for n in nums:
            counter = 0
            if (n-1) in nums:
                continue
            else:
                while n in nums:
                    counter += 1
                    n += 1
                longest = max(longest,counter)
        return longest