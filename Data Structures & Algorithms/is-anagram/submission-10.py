class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        c = defaultdict(int)

        for i in range(len(s)):
            c[s[i]] += 1
            c[t[i]] -= 1
        
        for v in c.values():
            if v != 0: return False
        
        return True