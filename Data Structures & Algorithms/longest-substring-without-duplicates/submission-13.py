class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cWindow = set()
        l = 0
        r = 0
        best = 0

        while r < len(s):
            while s[r] in cWindow:
                cWindow.remove(s[l])
                l+= 1
            cWindow.add(s[r])
            r += 1
            best = max(best, r - l)
        
        return best
