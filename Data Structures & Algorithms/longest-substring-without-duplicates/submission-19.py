class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        iMap = defaultdict(int)
        best = 0
        cur = 0

        for i, c in enumerate(s):
            if c in iMap and l <= iMap[c]:
                l = iMap[c]+1
            iMap[c] = i
            best = max(best, i - l + 1)
        
        return best