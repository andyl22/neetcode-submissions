class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for n in nums:
            if n+1 in nums:
                continue
            counter = 1
            while n-1 in nums:
                n = n-1
                counter += 1
            
            longest = max(counter,longest)
        return longest
