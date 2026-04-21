class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        top = 0
        counter = 0
        for n in nums:
            if n == 1:
                counter += 1
                top = max(counter, top)
            else:
                counter = 0
        return top