class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If s is empty, it's always a subsequence
        if not s:
            return True
        i=0
        for c in s:
            while len(t)>i and t[i] != c:
                i += 1
            if i == len(t):
                return False
            i += 1
        return True
