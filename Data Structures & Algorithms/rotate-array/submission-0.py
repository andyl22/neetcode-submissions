class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        start = 0
        curr = nums[0]

        while count < len(nums):
            prevIndex = start
            prevValue = nums[prevIndex]

            while True:
                nextIndex = (prevIndex + k)%len(nums)
                nums[nextIndex], prevValue = prevValue, nums[nextIndex]
                prevIndex = nextIndex
                count += 1
                if prevIndex == start:
                    break
            start += 1
    
