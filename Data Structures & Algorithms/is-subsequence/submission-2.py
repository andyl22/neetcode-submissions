class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        r=0
        for c in s:
            while len(t) and t[0] != c:
                t = t[1:]
            if not len(t):
                return False
            t = t[1:]
        return True