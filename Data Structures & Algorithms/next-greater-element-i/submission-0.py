class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            found = False
            for j in range(len(nums2)):
                if nums2[j] == i:
                    if j  == len(nums2)-1:
                        res.append(-1)
                    found = True
                    continue
                if found and nums2[j] > i:
                    res.append(nums2[j])
                    break
                elif j == len(nums2)-1:
                    res.append(-1)
        return res
