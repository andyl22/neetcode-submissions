class Solution:
    def validPalindrome(self, s: str, alive=True) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            if s[l] != s[r]:
                if alive:
                    return self.validPalindrome(s[l+1:r+1], False) or self.validPalindrome(s[l:r], False)
                else:
                    return False
            l += 1
            r -= 1
        return True