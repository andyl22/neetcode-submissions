class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        cand1, cand2 = None, None
        count1, count2 = 0, 0

        for n in nums:
            if cand1 == n:
                count1 += 1
            elif cand2 == n:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Verification pass: count only the specific candidates (O(1) space)
        res = []
        threshold = len(nums) // 3
        
        if cand1 is not None and nums.count(cand1) > threshold:
            res.append(cand1)
        if cand2 is not None and cand2 != cand1 and nums.count(cand2) > threshold:
            res.append(cand2)
            
        return res