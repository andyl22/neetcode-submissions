class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i, c in enumerate(s):
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for i, c in enumerate(t):
            if c in count and count[c] > 0:
                count[c] -= 1
            else:
                return False
        return True
