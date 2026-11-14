class Solution:
    def validPalindrome(self, s: str, evaluated=False) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                if evaluated == True:
                    return False
                return self.validPalindrome(s[l+1:r+1], True) or self.validPalindrome(s[l:r], True)
            l += 1
            r -= 1

        return True