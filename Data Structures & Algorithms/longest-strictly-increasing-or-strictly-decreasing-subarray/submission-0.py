class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums: return 0
        
        # We start with 1 because a single element is a subarray of length 1
        longest = 1 
        inc = 1
        dec = 1
        
        # The 'Vector' shift simulation:
        # We pair each element with its previous one
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            
            if diff > 0:
                inc += 1
                dec = 1
            elif diff < 0:
                dec += 1
                inc = 1
            else: # diff == 0
                inc = 1
                dec = 1
            
            longest = max(longest, inc, dec)
            
        return longest