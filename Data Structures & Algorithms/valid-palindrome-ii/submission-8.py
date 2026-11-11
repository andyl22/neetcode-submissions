class Solution:
    def validPalindrome(self, s: str, runAlready=False) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            if s[l] != s[r]:
                if runAlready:
                    return False
                return self.validPalindrome(s[l+1:r+1], True) or self.validPalindrome(s[l:r], True)
            l += 1
            r -= 1

        return True