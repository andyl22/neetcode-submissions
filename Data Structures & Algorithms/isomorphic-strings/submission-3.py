class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()

        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] in used:
                    return False
                mapping[s[i]] = t[i]
                used.add(t[i])
            else:
                if mapping[s[i]] != t[i]:
                    return False
        return True