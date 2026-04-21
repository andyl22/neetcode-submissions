class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # find a duplicate in the window. maintain a set

        i = 0
        j = 0
        chars = set()
        while j < len(nums):
            if j - i <= k:
                if nums[j] in chars:
                    return True
                chars.add(nums[j])
                j += 1
            else:
                chars.remove(nums[i])
                i += 1
        
        return False