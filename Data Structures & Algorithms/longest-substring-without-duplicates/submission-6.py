class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        j = 0
        i = 0

        seen = {}

        while j < len(s):
            if s[j] in seen:
                i = max(i, seen[s[j]] + 1)
            seen[s[j]] = j
            j += 1
            best = max(best, (j-i))
        
        return best