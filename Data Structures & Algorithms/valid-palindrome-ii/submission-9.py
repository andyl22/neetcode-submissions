class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l: int, r: int, deleted: bool) -> bool:
            while l < r:
                if s[l] != s[r]:
                    if deleted:
                        return False
                    # Try skipping either the left or the right character
                    return check(l + 1, r, True) or check(l, r - 1, True)
                l += 1
                r -= 1
            return True

        return check(0, len(s) - 1, False)