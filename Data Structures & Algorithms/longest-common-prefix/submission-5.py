class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for s in strs:
            if len(s) == 0:
                return ""
            for c in range(len(longest)):
                if c > len(s)-1:
                    longest = s
                    break
                if longest[c] != s[c]:
                    longest = longest[:c]
                    break
        return longest
