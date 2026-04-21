class Solution:
    def validPalindrome(self, s: str) -> bool:
        # at first I thought we could iterate down until we got to 3 chars remaining
        # then I remember the outlier could be at the edge... abbbbbbca

        # i think the solution is to handle this as we iterate through the string
        # if we encounter a mismatch, we check the l+1, r-1 to see if either would be a match
        # then we have a flag that will indicate if we'e deleted something already
        # if true, then return False

        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # Option 1: Skip the left character and check the rest
                # Option 2: Skip the right character and check the rest
                return self.is_palindrome(s, l + 1, r) or self.is_palindrome(s, l, r - 1)
            l += 1
            r -= 1
            
        return True

    def is_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
            
