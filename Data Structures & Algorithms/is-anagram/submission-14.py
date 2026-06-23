class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        cMap = defaultdict(int)
        for i in range(len(s)):
            cMap[s[i]] += 1
            cMap[t[i]] -= 1
        for v in cMap.values():
            if v != 0:
                return False
        return True
        