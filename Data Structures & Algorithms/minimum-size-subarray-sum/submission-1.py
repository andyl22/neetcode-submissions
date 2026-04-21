class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window problem
        # we want to minimize the window while sum > target

        left = 0
        total = 0
        n = len(nums)
        minLen = n + 1

        for i in range(n):
            total += nums[i]
            while total >= target:
                if total >= target:
                    minLen = min(minLen, i-left+1)
                total -= nums[left]
                left += 1

        
        return minLen % (n+1)
