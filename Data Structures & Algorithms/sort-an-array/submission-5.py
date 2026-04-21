class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        return self.merge(self.sortArray(left), self.sortArray(right))
    
    def merge(self, left, right):
        l_len = len(left)
        r_len = len(right)
        i = 0
        j = 0
        res = []
        while i < l_len and j < r_len:
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        return res + left[i:] + right[j:]