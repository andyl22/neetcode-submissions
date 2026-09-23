class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1,p2,p3 = m-1, n-1, m+n-1

        while p1 >= 0 or p2 >= 0:
            if p2 < 0 or p3 < 0:
                break
            n1 = nums1[p1] if p1 >= 0 else float('-inf')
            n2 = nums2[p2]
            if n1 > n2:
                nums1[p3] = n1
                p1 -= 1
            else:
                nums1[p3] = n2
                p2 -= 1
            p3 -= 1