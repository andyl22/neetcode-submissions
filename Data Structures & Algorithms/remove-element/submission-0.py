class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        # 'i' acts as the fast pointer, iterating through all elements.
        for i in range(len(nums)):
            # If the current element should be KEPT...
            if nums[i] != val:
                # 1. Move the 'kept' element to the k-th position.
                nums[k] = nums[i]
                # 2. Increment k to prepare for the next 'kept' element.
                k += 1
                
        # The value of k is the count of elements that were kept,
        # which is the new length of the modified array.
        return k
        