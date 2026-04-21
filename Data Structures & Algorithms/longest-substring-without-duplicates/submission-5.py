class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        j = 0
        i = 0

        seen = set()

        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            j += 1
            best = max(best, (j-i))
        
        return best