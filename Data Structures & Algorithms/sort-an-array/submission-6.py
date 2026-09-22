class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        l = nums[:mid]
        r = nums[mid:]

        return self.merge(self.sortArray(l), self.sortArray(r))

    def merge(self, l, r):
        l_len = len(l)
        r_len = len(r)

        i = 0
        j = 0

        res = []

        while i < l_len and j < r_len:
            if l[i] > r[j]:
                res.append(r[j])
                j += 1
            else:
                res.append(l[i])
                i += 1
        
        return res + l[i:] + r[j:]