class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i,c in enumerate(strs[0]):
            for s in strs:
                if i > len(s)-1:
                    return prefix
                if s[i] != c:
                    return prefix
            prefix += c
        return prefix


