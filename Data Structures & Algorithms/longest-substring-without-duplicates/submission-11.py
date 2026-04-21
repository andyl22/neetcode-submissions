class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window. we want to update the left pointer to the index of the repeated character 
        # and reset the length counter
        l = 0
        seen = {}
        longest = 0

        for i, c in enumerate(s):
            if c in seen:
                l = max(l, seen[c]+1)
            seen[c] = i
            longest = max(longest, i - l + 1)
        return longest
