class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            c = ""
            for s in strs:
                if i > len(s)-1:
                    return prefix
                if not c:
                    c = s[i]
                if c != s[i]:
                    return prefix
            prefix += c
        return prefix


