class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first idea.
        #   iterate through the array. for each element
        #   add that to a map with a value
        #   find the number before the current, increment by 1
        #   if there is a number after, increment that by 1
        #   but this can not work because you have to update all sequences
        #   e.g. you can have 2, increment the value of 3. but it wont update 4,5,6,etc.
        
        # second idea
        #   multiple arrays. but how would you have to iterate over every subarray
        #   this would violate the O(n) requirement
        
        # solution
        #   visit every element in the array via for loop
        #   for each element, check if the precedent exists
        #   if the precedent exists, start counting by searching
        #   convert nums into a hashset so it's not n^2
        nums = set(nums)
        longest = 0

        for n in nums:
            counter = 0
            if (n-1) in nums:
                continue
            else:
                while n in nums:
                    counter += 1
                    n += 1
                longest = max(counter, longest)
        return longest

        