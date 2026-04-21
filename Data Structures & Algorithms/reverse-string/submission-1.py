class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
# Initialize the left pointer (start) and right pointer (end)
        left, right = 0, len(s) - 1

        # Loop while the pointers haven't crossed each other
        while left < right:
            # Swap the elements at the left and right pointers
            s[left], s[right] = s[right], s[left]

            # Move the pointers one step closer to the center
            left += 1
            right -= 1
        
        # The list 's' is now reversed in place
        return s

