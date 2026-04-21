class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0
        
        for right in range(len(nums)):
            # 1. Maintain the window size: 
            # If the distance between right and left exceeds k, 
            # remove the element at the 'left' pointer.
            if right - left > k:
                window.remove(nums[left])
                left += 1
            
            # 2. Check the condition:
            # If the current number is already in the window, 
            # we found a duplicate within distance k.
            if nums[right] in window:
                return True
            
            # 3. Add the current number to the window
            window.add(nums[right])
            
        return False