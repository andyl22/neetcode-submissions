class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] in seen:
                return True
            seen.add(nums[j])
            if j - i >= k:
                seen.remove(nums[i])
                i += 1
            
            
            j += 1
        
        return False
            