class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cPrefix = ""

        for i, v in enumerate(strs[0]):
            for s in strs:
                if i >= len(s) or v != s[i]:
                    return cPrefix
            
            cPrefix += v
        
        return cPrefix

