class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        i = 0

        seen = {}

        for j in range(len(s)):
            if s[j] in seen:
                i = max(i, seen[s[j]] + 1)
            seen[s[j]] = j
            best = max(best, (j-i+1))
        
        return best