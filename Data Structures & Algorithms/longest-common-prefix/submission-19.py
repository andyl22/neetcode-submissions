class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for c in range(len(strs[0])):
            for s in strs:
                if len(s)-1 < c:
                    return prefix
                elif strs[0][c] != s[c]:
                    return prefix
            prefix += strs[0][c]
        
        return prefix
                