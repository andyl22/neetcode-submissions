class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cMap = {}
        i = 0
        j = 0
        best = 0

        while j < len(s):
            c = s[j]
            if c in cMap:
                i = max(cMap[c]+1, i)
            cMap[c] = j
            best = max(best,j-i+1)
            j += 1
        
        return best

