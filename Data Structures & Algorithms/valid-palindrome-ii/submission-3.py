class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            tempL = l + 1
            tempR = r
            if s[l] != s[r]:
                leftValid = True
                rightValid = True
                while tempL < tempR:
                    if s[tempL] != s[tempR]:
                        leftValid = False
                    tempL += 1
                    tempR -= 1
                r -= 1
                while l < r:
                    if s[l] != s[r]:
                        rightValid = False
                    l += 1
                    r -= 1
                return leftValid or rightValid
            l += 1
            r -= 1
        return True