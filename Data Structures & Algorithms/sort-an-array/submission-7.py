from collections import deque

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2

        return self.merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))
        
    def merge(self, left, right):
        res = []
        left=deque(left)
        right=deque(right)
        while left and right:
            if left[0] < right[0]:
                res.append(left.popleft())
            else:
                res.append(right.popleft())
        
        res.extend(left or right)
        return res
