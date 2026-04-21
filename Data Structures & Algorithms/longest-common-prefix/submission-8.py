class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""

        for i, c in enumerate(strs[0]):
            for s in strs:
                if i >= len(s):
                    return longest
                if s[i] != c:
                    return longest
            longest += c
        return longest