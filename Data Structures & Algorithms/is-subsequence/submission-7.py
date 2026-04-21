class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If s is empty, it's always a subsequence
        if not s:
            return True
        i=0
        for c in t:
            if c == s[i]:
                i += 1
            if i>=len(s):
                return True

        return i == len(s)
