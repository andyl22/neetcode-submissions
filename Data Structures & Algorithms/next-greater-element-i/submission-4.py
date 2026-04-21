class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        stack = []
        nextGreater = {}
        for n in nums2:
            while len(stack) and n > stack[-1]:
                nextGreater[stack.pop()] = n
            stack.append(n)
        
        for n in nums1:
            if n in nextGreater:
                res.append(nextGreater[n])
            else:
                res.append(-1)

        return res