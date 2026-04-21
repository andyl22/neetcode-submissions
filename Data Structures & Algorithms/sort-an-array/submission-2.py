class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        return self.mergeSorted(self.sortArray(left), self.sortArray(right))

    def mergeSorted(self, left, right):
        i = 0
        j = 0
        res = []
        while i <= len(left)-1 and j <= len(right)-1:
            if left[i] > right[j]:
                res.append(right[j])
                j += 1
            else:
                res.append(left[i])
                i += 1
        
        return res + left[i:] + right[j:]