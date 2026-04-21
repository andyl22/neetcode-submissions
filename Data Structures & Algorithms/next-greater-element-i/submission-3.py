class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            found = False
            ans = -1
            for j in range(len(nums2)):
                if nums2[j] == i:
                    found = True
                    continue
                if found and nums2[j] > i:
                    ans = nums2[j]
                    break
            res.append(ans)
        return res
