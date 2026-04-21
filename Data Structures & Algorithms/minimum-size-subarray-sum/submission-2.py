class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window problem
        # we want to minimize the window while sum > target

        left = 0
        total = 0
        minLen = float('inf')

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                if total >= target:
                    minLen = min(minLen, i-left+1)
                total -= nums[left]
                left += 1

        
        return minLen if minLen != float('inf') else 0
