class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        seen = set()

        for i in range(len(nums)):
            if i -l > k:
                seen.remove(nums[l])
                l += 1
            
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        
        return False