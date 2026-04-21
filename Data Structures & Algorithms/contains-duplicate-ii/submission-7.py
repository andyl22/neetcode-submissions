class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 0
        cur = set()

        while j < len(nums)-1:
            while j-i<=k:
                v = nums[j]
                if v in cur:
                    return True
                cur.add(v)
                j+=1
            
            cur.remove(nums[i])
            i+=1
        if nums[j] in cur:
            return True

        return False
