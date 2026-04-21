class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # iterate over the string with two pointers
        # when fast pointer == same char as slow pointer
        # move slow pointer until we get to the next unique pointer
        # store the longest length as we iterate
        slow = 0
        fast = 0
        longest = 0
        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                slow = max(slow, seen[s[i]]+1)
            fast += 1
            seen[s[i]] = i
            longest = max(longest, fast - slow)

        return longest