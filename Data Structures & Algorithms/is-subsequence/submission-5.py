class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If s is empty, it's always a subsequence
        if not s:
            return True
        i=0
        for c in t:
            if i<len(s) and c == s[i]:
                i += 1

        return i == len(s)
