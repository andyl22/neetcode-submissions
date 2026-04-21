class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window. we want to update the left pointer to the index of the repeated character 
        # and reset the length counter
        l = 0
        seen = set()
        longest = 0

        for i, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            longest = max(longest, i+1 - l)
        return longest
