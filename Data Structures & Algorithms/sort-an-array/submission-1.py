class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lenNums = len(nums)
        # return list as is once we hit base case. only 2 ele in list
        if lenNums == 1:
            return nums

        mid = lenNums//2
        left = nums[:mid]
        right = nums[mid:]

        sorted_left = self.sortArray(left)
        sorted_right = self.sortArray(right)
        return self.merge(sorted_left, sorted_right)

    def merge(self, left, right):
        res = []
        i=0
        j=0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                res.append(right[j])
                j += 1
            else:
                res.append(left[i])
                i += 1
        return res + left[i:] + right[j:]