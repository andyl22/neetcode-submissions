class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # we build the slow array
        # if there is no duplicate, we want to start writing the actual array
        # if there is a duplicate, do not write anything
        # since it is ordered, we don't need to worry about the element values being separated. can always check last element
        slow = 1

        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow
            
