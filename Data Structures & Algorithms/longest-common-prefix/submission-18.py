class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""

        for i,c in enumerate(strs[0]):
            cur = c
            for s in strs:
                if i > len(s)-1 or cur != s[i]:
                    return longest
            longest += cur
        
        return longest